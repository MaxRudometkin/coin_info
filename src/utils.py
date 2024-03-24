def html_template(rows, name):
    html = """
        <span class="selected"></span></br>
        <input type="text" id="{}-input" style="width:100%" onkeyup="filterTable(this.id)">
        <table id="{}-table" style="width:100%">
        <thead>
            <tr>
                <th class="value-cell" onclick="sortTable('{}-table', 0)">value</th>
                <th onclick="sortTable('{}-table', 1)">count</th>
                <th onclick="sortTable('{}-table', 2)">%</th>
                <th onclick="sortTable('{}-table', 3)">Market Cap.</th>
            </tr>
        </thead>
        <tbody>
    """.format(name, name, name, name, name, name)

    for row in rows:
        html += f'<tr onclick="clickOnValue(this,\'{name}\')">'
        html += f'<td class="value-cell">{row[0]}</td>'
        html += f'<td class="count-cell">{row[1]}</td>'
        html += f'<td class="percent-cell">{row[2]}</td>'
        html += f'<td class="m-cap-cell">{row[3]}</td></tr>'

    return html + '</tbody></table>'
