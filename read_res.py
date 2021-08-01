import 	xlrd
def readAnswers(path=None):
	if path==None or path=='':
		path = './dapan/dapan.xlsx'
	res_file = xlrd.open_workbook(path)
	sheet = res_file.sheet_by_index(0)
	COL_RES = 6
	# print(sheet.row_values(1))
	# print(sheet.nrows)
	data = []
	for row in range(sheet.nrows):
		row_val = sheet.cell(row,COL_RES).value
		data.append(row_val.split(','))

	dict_data = {data[i][0] :data[i][1:]  for i in range(len(data)) }
	# print(dict_data['7_2010'])

	# print(data)
	return dict_data
readAnswers()