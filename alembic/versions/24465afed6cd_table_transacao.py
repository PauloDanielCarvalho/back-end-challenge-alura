"""table_transacao

Revision ID: 24465afed6cd
Revises: 
Create Date: 2022-07-05 22:36:39.159117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24465afed6cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaçoes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('banco_origem', sa.String(), nullable=True),
    sa.Column('agencia_origem', sa.Integer(), nullable=True),
    sa.Column('conta_origem', sa.String(), nullable=True),
    sa.Column('banco_destino', sa.String(), nullable=True),
    sa.Column('agencia_destino', sa.Integer(), nullable=True),
    sa.Column('conta_destino', sa.String(), nullable=True),
    sa.Column('valor_transação', sa.Float(), nullable=True),
    sa.Column('data_hora', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaçoes')
    # ### end Alembic commands ###