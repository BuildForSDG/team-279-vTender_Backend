"""empty message

Revision ID: 8b3422f22cd9
Revises: 
Create Date: 2020-06-02 01:10:33.361899

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '8b3422f22cd9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tenders',
    sa.Column('tender_id', sa.Integer(), nullable=False),
    sa.Column('tenderNumber', sa.String(length=25), nullable=False),
    sa.Column('tenderDescription', sa.String(length=80), nullable=False),
    sa.Column('category', sa.String(length=40), nullable=False),
    sa.Column('datePublished', sa.String(length=15), nullable=False),
    sa.Column('closingDate', sa.String(length=15), nullable=False),
    sa.Column('tenderStatus', sa.String(length=10), nullable=False),
    sa.Column('nameOfInstitution', sa.String(length=60), nullable=False),
    sa.Column('officalLocation', sa.String(length=60), nullable=False),
    sa.Column('InstitutionContactPerson', sa.String(length=60), nullable=False),
    sa.Column('InstitutionPersonEmail', sa.String(length=60), nullable=False),
    sa.Column('InstitutionPersonPhone', sa.String(length=60), nullable=False),
    sa.Column('global_apply_count', sa.Integer(), nullable=True),
    sa.Column('global_winning_count', sa.Integer(), nullable=True),
    sa.Column('company_names', sqlite.JSON(), server_default='{}', nullable=True),
    sa.PrimaryKeyConstraint('tender_id'),
    sa.UniqueConstraint('tenderNumber')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_first_name'), 'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('company',
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('companyName', sa.String(length=60), nullable=False),
    sa.Column('companyRegistrationNo', sa.String(length=50), nullable=False),
    sa.Column('directors', sa.String(length=60), nullable=False),
    sa.Column('company_phone_number', sa.String(length=15), nullable=False),
    sa.Column('companyAddress', sa.String(length=50), nullable=False),
    sa.Column('apply_count', sa.Integer(), nullable=True),
    sa.Column('winning_count', sa.Integer(), nullable=True),
    sa.Column('is_winner', sa.Boolean(), server_default='false', nullable=True),
    sa.Column('awardedPoint', sa.Integer(), nullable=True),
    sa.Column('tenderNumber', sa.String(length=25), nullable=False),
    sa.Column('tender_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tender_id'], ['tenders.tender_id'], ),
    sa.PrimaryKeyConstraint('company_id'),
    sa.UniqueConstraint('apply_count'),
    sa.UniqueConstraint('companyRegistrationNo'),
    sa.UniqueConstraint('company_phone_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('tenders')
    # ### end Alembic commands ###
