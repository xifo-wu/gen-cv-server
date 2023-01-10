from flask import abort
from app.api.v1 import api_v1
from app.models.resume import Resume
from app.extensions import db
from app.schemas.resume import CreateAndResumeSchema, ResumeSchema
from lib import response
from lib.request import load_schema
from flask_jwt_extended import jwt_required, get_current_user

resume_schema = ResumeSchema()


@api_v1.get('/resumes')
@jwt_required()
def index():
    current_user = get_current_user()
    resumes_select = db.select(Resume).where(
        Resume.user_id == current_user['id']).order_by(Resume.updated_at)

    # TODO 添加 page per_page query
    resumes_pagination = db.paginate(
        select=resumes_select, per_page=10)
    print(resumes_pagination.items, "aaaaaaaa")

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
    })


@api_v1.post('/resumes')
@jwt_required()
def create():
    current_user = get_current_user()
    schema = load_schema(CreateAndResumeSchema())

    resume = Resume(
        name=schema['name'],
        slug=schema['slug'],
        layout_type=schema['layout_type'],
        module_order=schema['module_order'],
        theme_color=schema['theme_color'],
        user_id=current_user['id'],
    )

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
