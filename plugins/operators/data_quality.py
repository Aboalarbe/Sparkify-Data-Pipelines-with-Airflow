from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift = "",
                 tables = [],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift = redshift
        self.tables = tables

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift)
        for table in self.tables:
            records = redshift.get_records("SELECT COUNT(*) FROM {}".format(table))             
            if len(records) < 1 or len(records[0]) < 1:
                self.log.error("{} IS EMPTY !!".format(table))
                raise ValueError("Data Quality JOB failed. {} IS EMPY !!".format(table))
            num_records = records[0][0]
            if num_records == 0:
                self.log.error("EMPTY TABLE {}".format(table))
                raise ValueError("Zero records present in {}".format(table))
            self.log.info("Data quality JOB on table {} check passed successfully with {} records".format(table, num_records))