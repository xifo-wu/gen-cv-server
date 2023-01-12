"""Add Resume Basic and field Table

Revision ID: 02454d9f45ac
Revises: 5b807dca990d
Create Date: 2023-01-12 09:22:15.081156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02454d9f45ac'
down_revision = '5b807dca990d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resume_basic_field',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('value', sa.String(length=255), nullable=True),
    sa.Column('label', sa.String(length=255), nullable=True),
    sa.Column('icon', sa.String(length=50), nullable=True),
    sa.Column('is_show_label', sa.Boolean(), nullable=True),
    sa.Column('is_show_icon', sa.Boolean(), nullable=True),
    sa.Column('sort_index', sa.Float(), nullable=True),
    sa.Column('visible', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resume_basic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('resume_id', sa.Integer(), nullable=True),
    sa.Column('email_id', sa.Integer(), nullable=True),
    sa.Column('name_id', sa.Integer(), nullable=True),
    sa.Column('age_id', sa.Integer(), nullable=True),
    sa.Column('birthday_id', sa.Integer(), nullable=True),
    sa.Column('avatar_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('job_year_id', sa.Integer(), nullable=True),
    sa.Column('mobile_id', sa.Integer(), nullable=True),
    sa.Column('website_id', sa.Integer(), nullable=True),
    sa.Column('educational_qualifications_id', sa.Integer(), nullable=True),
    sa.Column('in_a_word_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['age_id'], ['resume_basic_field.id'], ),
    sa.ForeignKeyConstraint(['avatar_id'], ['resume_basic_field.id'], ),
    sa.ForeignKeyConstraint(['birthday_id'], ['resume_basic_field.id'], ),
    sa.ForeignKeyConstraint(['educational_qualifications_id'], ['resume_basic_field.id'], ),
    sa.ForeignKeyConstraint(['email_id'], ['resume_basic_field.id'], ),
    sa.ForeignKeyConstraint(['in_a_word_id'], ['resume_basic_field.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['resume_basic_field.id'], ),
    sa.ForeignKeyConstraint(['job_year_id'], ['resume_basic_field.id'], ),
    sa.ForeignKeyConstraint(['mobile_id'], ['resume_basic_field.id'], ),
    sa.ForeignKeyConstraint(['name_id'], ['resume_basic_field.id'], ),
    sa.ForeignKeyConstraint(['resume_id'], ['resume.id'], ),
    sa.ForeignKeyConstraint(['website_id'], ['resume_basic_field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resume_basic')
    op.drop_table('resume_basic_field')
    # ### end Alembic commands ###