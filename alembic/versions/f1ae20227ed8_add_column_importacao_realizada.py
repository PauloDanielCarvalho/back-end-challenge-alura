"""add Column importacao_realizada

Revision ID: f1ae20227ed8
Revises: 9e78edd84dc9
Create Date: 2022-07-11 20:29:52.734458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1ae20227ed8'
down_revision = '9e78edd84dc9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('importacao_realizada',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('data_transacao', sa.DateTime(), nullable=True),
    sa.Column('data_importacao', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Pessoa')
    op.add_column('transaçoes', sa.Column('data_transacao', sa.DateTime(), nullable=True))
    op.drop_column('transaçoes', 'data_hora')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaçoes', sa.Column('data_hora', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('transaçoes', 'data_transacao')
    op.create_table('Pessoa',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Pessoa_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Pessoa_pkey')
    )
    op.drop_table('importacao_realizada')
    # ### end Alembic commands ###
