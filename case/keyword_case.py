import sys
sys.path.append('D:\\Imooc_selenium')
from util.Excelreader import ExcelDate
from keywords.actionMethod import ActionMethod

class KeywordCase:
    def run_main(self):
        handle_excel = ExcelDate('D:\\Imooc_selenium\\config\\keywords.xls','Sheet1')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_value(i,3)
                if is_run == 'yes':
                    method = handle_excel.get_col_value(i,4)#使用的方法
                    send_value = handle_excel.get_col_value(i,5)#输入的数据
                    handle_value = handle_excel.get_col_value(i,6)#key
                    

if __name__ == '__main__':
    obj = KeywordCase()
    obj.run_main()