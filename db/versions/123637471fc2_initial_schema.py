"""initial schema

Revision ID: 123637471fc2
Revises: None
Create Date: 2014-08-26 02:17:36.673082

"""

# revision identifiers, used by Alembic.
revision = '123637471fc2'
down_revision = None

from alembic import op
import sqlalchemy as sa

def upgrade():

    op.create_table(
        'assets',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('type', sa.String(50)),
        sa.Column('asset_text', sa.TEXT),
        sa.Column('asset_binary', sa.BLOB),
        mysql_engine="MyISAM"

    )

    print 'Manual Step Required:'
    print " --> mysql -uroot -p -e 'CREATE FULLTEXT INDEX idx ON assets(asset_text)' flask_asset"

def downgrade():
    op.drop_table('asset')
