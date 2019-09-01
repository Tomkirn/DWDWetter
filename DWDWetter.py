import ui
import requests
from datetime import date
global index

url = 'https://opendata.dwd.de/weather/text_forecasts/txt/'
stations = ['DWEH', 'DWHG', 'DWHH']


def readDWDreportList(DWDStation):
	req = requests.request('GET', url)
	pass


def uiListDataSouceAction(sender):
	req2 = requests.request('GET', url + 'ber01-VHDL13_' + stations[index] + '_' + files[sender.selected_row])
	uiText.text = req2.text.replace('\r', '')


def uiSegmentedControlAction(sender):
	index = sender.selected_index
	uiTable.reload


index = 0

# DWEH = Nordrhein Westfalen
# DWHG = Niedersachsen / Bremen
# DWHH = Schleswig Holstein / Hamburg

# datetoday = date.today()
# dateday = datetoday.day

files = []
txtfiles = []

req = requests.request('GET', url)

for line in req.iter_lines():
	if line.decode('UTF-8').find('ber01-VHDL13_DWHG') > 0:
		file = line.decode('UTF-8').split('<')[1].split('>')[1][18:]
		files.append(file)

files.sort

for file in files:
	txtfiles.append(file.split('-')[1][0:6]+' '+file.split('-')[1][6:11])

#
# ---------- UI ----------
#

v = ui.load_view()
v.present(style='fullscreen', hide_title_bar=True)

uiText = v['textview1']
uiTable = v['tableview1']
uiSelector = v['segmentedcontrol1']

uiText.text = '---'
uiListDataSource = ui.ListDataSource(txtfiles)
uiListDataSource.action = uiListDataSouceAction

uiTable.data_source = uiListDataSource
uiTable.delegate = uiListDataSource
uiTable.reload()

uiSelector.action = uiSegmentedControlAction
