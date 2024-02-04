"""
Example - Excel ETL
"""

# Preparation
import typing
import logging
import pandas

def extract() -> typing.Tuple[pandas.DataFrame, pandas.DataFrame]:
    """
    Extract

    :return: data tables extracted from excel sheets and load in-memory as pandas dataframe/table
    :rtype: typing.Tuple[pandas.DataFrame, pandas.DataFrame]
    """
    logger = logging.getLogger(__name__)
    logger.info('Extract: Begin')

    df_sh1_extract = pandas.read_excel(io = './Example_ETLExcel_I.xlsx', sheet_name = 'Sh1')
    df_sh2_extract = pandas.read_excel(io = './Example_ETLExcel_I.xlsx', sheet_name = 'Sh2')
    
    logger.info('Extract: Done')
    return df_sh1_extract, df_sh2_extract

def transform(df_sh1_extract: pandas.DataFrame, df_sh2_extract: pandas.DataFrame) -> typing.Tuple[pandas.DataFrame, pandas.DataFrame]:
    """
    Transform

    :param df_sh1_extract: first excel sheet loaded in-memory pandas dataframe/table
    :type df_sh1_extract: pandas.DataFrame
    :param df_sh2_extract: sheet excel sheet loaded in-memory pandas dataframe/table
    :type df_sh2_extract: pandas.DataFrame
    :return: transformed dataframes
    :rtype: typing.Tuple[pandas.DataFrame, pandas.DataFrame]
    """
    logger = logging.getLogger(__name__)
    logger.info('Transform: Begin')

    columns_to_keep_df_sh1 = ['ColA', 'Col2']
    df_sh1_toload = df_sh1_extract[columns_to_keep_df_sh1].copy(deep = True)

    columns_to_keep_df_sh2 = ['ColB', 'Col1', 'Col3']
    df_sh2_toload = df_sh2_extract[columns_to_keep_df_sh2].copy(deep = True)

    logger.info('Transform: Done')
    return df_sh1_toload, df_sh2_toload

def load(df_sh1_toload: pandas.DataFrame, df_sh2_toload: pandas.DataFrame) -> typing.NoReturn:
    """
    Load/Save

    :param df_sh1_toload: ready to save first dataframe
    :type df_sh1_toload: pandas.DataFrame
    :param df_sh2_toload: ready to save second dataframe
    :type df_sh2_toload: pandas.DataFrame
    :return: Nothing
    :rtype: typing.NoReturn
    """
    logger = logging.getLogger(__name__)
    logger.info('Load: Begin')

    with pandas.ExcelWriter('./Example_ETLExcel_O.xlsx') as df_to_excelsheet_writer:
        df_sh1_toload.to_excel(excel_writer = df_to_excelsheet_writer, sheet_name = 'ShA', index = False)
        df_sh2_toload.to_excel(excel_writer = df_to_excelsheet_writer, sheet_name = 'ShB', index = False)
    
    logger.info('Load: Done')
    return

def main() -> typing.NoReturn:
    """
    ETL

    :return: Nothing
    :rtype: typing.NoReturn
    """
    logger = logging.getLogger(__name__)
    logger.info('ETL: Begin')

    df_sh1_extract, df_sh2_extract = extract()
    df_sh1_toload, df_sh2_toload = transform(df_sh1_extract = df_sh1_extract, df_sh2_extract = df_sh2_extract)
    load(df_sh1_toload = df_sh1_toload, df_sh2_toload = df_sh2_toload)

    logger.info('ETL: Done')
    return

if __name__ == '__main__':
    main()
