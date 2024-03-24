import pandas as pd
from src.db_connect import db_engine
from src.utils import html_template


class MainDf:
    def __init__(self):
        self.limit = 100
        self.df = None
        self.read_data()

    def read_data(self):
        if self.limit:
            self.df = pd.read_sql(f'SELECT * FROM coins_info limit {self.limit}', db_engine)
        else:
            self.df = pd.read_sql('SELECT * FROM coins_info', db_engine)

    def show_keys(self, params=None) -> str:
        """
        Reads coins info from database.
        :return: coins info
        """
        temp_df = self.df
        if params:
            for fil in params['filters']:
                if '' in fil or len(fil) != 2: continue
                temp_df = temp_df[temp_df[fil[0]] == fil[1]]

        html = '<span class="selected"></span></br><table>'
        for column in temp_df.columns:
            unique_len = temp_df[column].nunique()
            html += f'<tr onclick="clickOnKey(this)"><td class="key-cell">{column}({unique_len})</td></tr>'
        return html + '</table>'

    def show_values(self, obj):

        temp_df = self.df
        # filters
        for fil in obj['filters']:
            if '' in fil or len(fil)!=2: continue
            temp_df = temp_df[temp_df[fil[0]] == fil[1]]

        value = obj['value']
        data = []
        for val in temp_df[value].unique():
            data.append([val, len(temp_df[temp_df[value] == val].index)])

        # add percentage
        total = sum([d[1] for d in data])
        for d in data:
            t = (d[1] / total) * 100
            d.append('{:.1f}'.format(t))

            m_cap = temp_df[temp_df[value] == d[0]]['market_cap_rank'].values[0]
            try:
                if m_cap == 'nan':
                    m_cap = 0
                m_cap = float(m_cap)
            except:
                m_cap = 0

            d.append(m_cap)


        # add market cap
        columns = ['id', 'name', 'web_slug']


        # sort
        if len(data) > 1:
            if value in columns:
                data.sort(key=lambda x: x[3], reverse=True)
            elif set([x for x in data[1]]) == {'1'}:
                data.sort(key=lambda x: x[0], reverse=True)
            else:
                data.sort(key=lambda x: x[1], reverse=True)

        html = html_template(data, value)

        return {'div_id': obj['div_id'], 'html': html}
