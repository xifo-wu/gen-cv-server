import uuid
import datetime
from flask import abort
from app.api.v1 import api_v1
from app.models import Education, EducationDetail
from app.models.resume import Resume
from app.models.resume_basic import ResumeBasic
from app.models.resume_basic_field import ResumeBasicField
from app.extensions import db
from app.schemas.education import EducationSchema, EducationDetailSchema
from app.schemas.resume import CreateAndResumeSchema, ResumeSchema, ResumeBasicSchema
from lib import response
from lib.request import load_schema
from flask_jwt_extended import jwt_required, get_current_user

resume_schema = ResumeSchema()
resume_basic_schema = ResumeBasicSchema()


def get_own_resume(resume_slug: str) -> Resume:
    # 只能更新自己的简历
    current_user = get_current_user()
    resume = db.one_or_404(db.select(Resume).filter_by(slug=resume_slug))

    if current_user['id'] != resume.user.id:
        abort(404)

    return resume


@api_v1.get('/resumes')
@jwt_required()
def index():
    # 只能获取到自己的简历
    current_user = get_current_user()
    resumes_select = db.select(Resume).where(
        Resume.user_id == current_user['id']).order_by(Resume.updated_at.desc())

    resumes_pagination = db.paginate(
        select=resumes_select, per_page=10
    )

    resumes_schema = ResumeSchema(many=True)
    result = resumes_schema.dump(resumes_pagination.items)
    return response.format(
        data=result,
        meta={
            "per_page": resumes_pagination.per_page,
            "total": resumes_pagination.total,
            "page": resumes_pagination.page,
            "has_prev": resumes_pagination.has_prev,
            "has_next": resumes_pagination.has_next,
        }
    )


@api_v1.post('/resumes')
@jwt_required()
def create():
    """
    创建简历时会自动创建基本信息
    """
    current_user = get_current_user()
    schema = load_schema(CreateAndResumeSchema())
    today = datetime.date.today()

    resume = Resume(
        name=schema['name'],
        slug=schema.get('slug') or uuid.uuid4().hex,
        layout_type=schema['layout_type'],
        module_order=schema['module_order'],
        theme_color=schema['theme_color'],
        user_id=current_user['id'],
    )

    # 新建一份简历基本信息
    resume.resume_basic = ResumeBasic(
        email=ResumeBasicField(
            value=current_user['email'], label="邮箱", visible=True
        ),
        name=ResumeBasicField(
            value=current_user['nickname'], label="姓名", visible=True
        ),
        mobile=ResumeBasicField(
            value=current_user.get('mobile'), label="电话", visible=True
        ),
        job=ResumeBasicField(
            value="产品经理", label="岗位", visible=True
        ),
        job_year=ResumeBasicField(
            value="3 年", label="工作经验", visible=True
        ),
    )

    # 新建一份默认教育经历
    resume.education = Education(
        label="教育经历",
        visible=True,
        content_type="education2",
        show_split=True,
        split="split1",
        education_details=[
            EducationDetail(
                name="嘿嘿大学",
                start_on=f"{today.year}-09",
                end_on=f"{today.year + 4}-06",
                university_majors="软件工程",
                desc="软件工程是一门研究用工程化方法构建和维护有效、实用和高质量的软件的学科。",
            )
        ])

    db.session.add(resume)
    db.session.commit()

    result = resume_schema.dump(resume)

    return response.format(data=result)


@api_v1.put('/resumes/<string:resume_slug>')
@jwt_required()
def update(resume_slug):
    schema = load_schema(CreateAndResumeSchema())
    # 只能更新自己的简历
    current_user = get_current_user()
    resume = db.one_or_404(db.select(Resume).filter_by(slug=resume_slug))

    if current_user['id'] != resume.user.id:
        abort(404)

    db.session.execute(
        db.update(Resume).where(Resume.id == resume.id).values(schema)
    )
    db.session.commit()

    result = resume_schema.dump(resume)
    return response.format(data=result)


@api_v1.delete('/resumes/<string:resume_slug>')
@jwt_required()
def destory(resume_slug):
    current_user = get_current_user()
    resume = db.one_or_404(db.select(Resume).filter_by(slug=resume_slug))

    if current_user['id'] != resume.user.id:
        abort(404)

    db.session.delete(resume)
    db.session.commit()

    return response.format(message="删除成功")


@api_v1.get('/resumes/<string:resume_slug>')
@jwt_required()
def show(resume_slug):
    current_user = get_current_user()
    resume = db.one_or_404(db.select(Resume).filter_by(slug=resume_slug))

    if current_user['id'] != resume.user.id:
        abort(404)

    result = resume_schema.dump(resume)
    return response.format(data=result)


@api_v1.put('/resumes/<string:resume_slug>/resume-basic')
@jwt_required()
def update_resume_basic(resume_slug):
    schema = load_schema(resume_basic_schema)
    resume = get_own_resume(resume_slug)
    resume.resume_basic = schema
    db.session.commit()

    result = resume_schema.dump(resume)

    return response.format(data=result)


@api_v1.put('/resumes/<string:resume_slug>/education')
@jwt_required()
def update_education(resume_slug):
    schema = load_schema(EducationSchema())
    resume = get_own_resume(resume_slug)
    resume.education = schema
    db.session.commit()

    result = resume_schema.dump(resume)

    return response.format(data=result)


@api_v1.put('/resumes/<string:resume_slug>/education-details/<string:education_detail_id>')
@jwt_required()
def update_education_detail(resume_slug, education_detail_id):
    schema = load_schema(EducationDetailSchema())
    resume = get_own_resume(resume_slug)

    education_detail = db.one_or_404(
        db.select(EducationDetail).filter_by(id=education_detail_id))

    if resume.education.id != education_detail.id:
        abort(403)

    db.session.execute(
        db.update(EducationDetail).where(EducationDetail.id == education_detail.id).values(
            EducationDetailSchema(exclude=("id", "updated_at", "created_at")).dump(schema))
    )
    db.session.commit()

    result = resume_schema.dump(resume)

    return response.format(data=result)


@api_v1.post('/resumes/<string:resume_slug>/education-details')
@jwt_required()
def create_education_detail(resume_slug):
    schema = load_schema(EducationDetailSchema())
    resume = get_own_resume(resume_slug)

    resume.education.education_details.append(schema)

    # db.session.add(schema)
    db.session.commit()

    result = resume_schema.dump(resume)

    return response.format(data=result)
