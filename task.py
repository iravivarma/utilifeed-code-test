import pandas as pd
from datetime import datetime
import glob, os

def aggregate_data(output_file):
    '''
    code tries... if file exists
    or else,
    it will enters into exception and creates a file.
    '''
    try:
        data_out = pd.read_csv(output_file)
        
    except:
        dates = ['2017-01-01 00:00:00',
                '2017-01-01 01:00:00',
                '2017-01-01 02:00:00',
                '2017-01-01 03:00:00',
                '2017-01-01 04:00:00',
                '2017-01-01 05:00:00',
                '2017-01-01 06:00:00',
                '2017-01-01 07:00:00',
                '2017-01-01 08:00:00',
                '2017-01-01 09:00:00',
                '2017-01-01 10:00:00',
                '2017-01-01 11:00:00',
                '2017-01-01 12:00:00',
                '2017-01-01 13:00:00',
                '2017-01-01 14:00:00',
                '2017-01-01 15:00:00',
                '2017-01-01 16:00:00',
                '2017-01-01 17:00:00',
                '2017-01-01 18:00:00',
                '2017-01-01 19:00:00',
                '2017-01-01 20:00:00',
                '2017-01-01 21:00:00',
                '2017-01-01 22:00:00',
                '2017-01-01 23:00:00']
        flow = [ 0 for i in range(0, 24)]
        temperature = [ 0 for i in range(0, 24)]
        data_out = pd.DataFrame({dates, flow, temperature}, columns = ['datetime', 'flow', 'temperature'])
    return data_out



def stream_aggregator(filename):
    data = pd.read_csv(filename)
    try:
        # print(data['datetime'])
        data = data[['flow', 'temperature']]
        #flow_sum stores the sum of the values of aggregate data's sum and data's flow column
        #print(data)
        data_out['flow'] = data_out['flow']+data['flow']
        #print(data_out['flow'])
        #product gives the product of aggreate_data flow and data's temperature column
        #print(data['temperature'])
        product = [a*b for a,b in zip(data['flow'], data['temperature'])]
        #print(product)
        # temp_wt_agg stores the weighted_sum of the values of temp_wt_agg and data's temperature column
        temp_wt_agg = [a+b for a,b in zip(data_out['temperature'], product)]
        #print(temp_wt_agg)

        # finally the aggreagation of flow_sum and temp_wt_agg is stored in temp_wt_agg
        data_out['temperature'] = temp_wt_agg  #[round(b/a, 2) for a,b in zip(data_out['flow'], temp_wt_agg)]
        #print(data_out[['flow', 'temperature']])
        #print(data_out['temperature'])
    except:
        return False
    return data_out['flow'], data_out['temperature']





source_path = './'
input_path = source_path+"input/"
output_path = "./output/"
output_file = "./output/stream_aggregate.csv"
temp = "./output/stream_aggregate_1.csv"
filenames = []
'''
for getting current dates hourly time series..........
'''
dates = datetime.today().strftime('%Y/%m/%d')
time = pd.date_range(str(dates), periods=24, freq='1H')
#collecting al the input file naes into filenames folder.....
for filename in glob.glob(os.path.join(input_path, '*.csv')):
        filenames.append(filename)

#storing the output data into data_out variable
data_out = aggregate_data(output_file)

#operation starts with each file name on stream_aggregator methods.
for filename in filenames:
        data_out['flow'], data_out['temperature'] = stream_aggregator(filename)

#finally diving the total sum of temperature by total flow and
#storing it in aggregate_data's temperature column.
data_out['temperature'] = [round(b/a, 2) for a,b in zip(data_out['flow'], data_out['temperature'])]
    
data_out.to_csv(temp,index=False)
