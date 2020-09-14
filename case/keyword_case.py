import sys
sys.path.append('D:\\Imooc_selenium')
from util.Excelreader import ExcelDate
from keywords.actionMethod import ActionMethod

class KeywordCase:
    def run_main(self):
        handle_excel = ExcelDate('D:\\Imooc_selenium\\config\\keywords.xls','Sheet1')
        case_lines = handle_excel.get_lines()