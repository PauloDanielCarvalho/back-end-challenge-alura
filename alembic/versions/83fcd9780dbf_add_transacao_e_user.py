"""add transacao e user

Revision ID: 83fcd9780dbf
Revises: 80ab02f31274
Create Date: 2022-07-19 18:58:59.303915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83fcd9780dbf'
down_revision = '80ab02f31274'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('importacao_realizada', sa.Column('id_user', sa.Integer(), nullable=True))
    op.add_column('importacao_realizada', sa.Column('id_transaçoes', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'importacao_realizada', 'transaçoes', ['id_transaçoes'], ['id'])
    op.create_foreign_key(None, 'importacao_realizada', 'users', ['id_user'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'importacao_realizada', type_='foreignkey')
    op.drop_constraint(None, 'importacao_realizada', type_='foreignkey')
    op.drop_column('importacao_realizada', 'id_transaçoes')
    op.drop_column('importacao_realizada', 'id_user')
    # ### end Alembic commands ###
