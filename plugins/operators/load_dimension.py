from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift = "",
                 table = "",
                 sql = "",        
                 append_only = False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift = redshift
        self.table = table
        self.sql = sql
        self.append_only = append_only

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift)
        if not self.append_only:
            self.log.info("TRUNCATE the table {} in the Redshift".format(self.table))
            redshift.run("DELETE FROM {}".format(self.table))  
        self.log.info("Satrt Insert into {} fact table".format(self.table))    
        insert_query = f"INSERT INTO {self.table} \n{self.sql}"
        redshift.run(insert_query)