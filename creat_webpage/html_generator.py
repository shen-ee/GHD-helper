import webbrowser
import os
import csv

html = '''
<!DOCTYPE html>
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <link rel="icon" href="https://getbootstrap.com/favicon.ico">
    <title>Grid Template for Bootstrap</title>
    <link rel="stylesheet" href="style.css">
  </head>

  <body>
    <div class="middle">
      <img class="demo" src="{img_name}" alt="final result">
      <hr>
      <table class="">
        <tbody>
          <tr>
            <th>Moster</th>
            <th><img class="icon" src="img/bruno.png" alt="bruno"></th>
            <th><img class="icon" src="img/compy.png" alt="compy"></th>
            <th><img class="icon" src="img/tina.png" alt="tina"></th>
            <th><img class="icon" src="img/petey.png" alt="petey"></th>        
          </tr>
          <tr>
            <td>Number</td>
            <td>{num_bruno}</td>
            <td>{num_compy}</td>
            <td>{num_tina}</td>
            <td>{num_petey}</td>
          </tr>
          <tr>
              <th>Towel</th>
              <th><img class="icon" src="img/teleport.png" alt="teleport"></th>
              <th><img class="icon" src="img/tesla.png" alt="tesla"></th>
              <th><img class="icon" src="img/laser.png" alt="laser"></th>
              <th><img class="icon" src="img/dj.png" alt="dj"></th>        
            </tr>
            <tr>
              <td>Number</td>
              <td>{num_teleport}</td>
              <td>{num_tesla}</td>
              <td>{num_laser}</td>
              <td>{num_dj}</td>
            </tr>
        </tbody>
      </table>
    </div>
  </body>

  </html>
'''

def gen_html():
  with open('number.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
    final = html.format(img_name="img/demo.png",
                        num_bruno = int(mydict['bruno']) if 'bruno' in mydict else 0,
                        num_compy = int(mydict['compy']) if 'compy' in mydict else 0,
                        num_tina = int(mydict['tina']) if 'tina' in mydict else 0,
                        num_petey = int(mydict['petey']) if 'petey' in mydict else 0,
                        num_teleport = int(mydict['teleport']) if 'teleport' in mydict else 0,
                        num_tesla = int(mydict['tesla']) if 'tesla' in mydict else 0,
                        num_laser = int(mydict['laser']) if 'laser' in mydict else 0,
                        num_dj = int(mydict['dj']) if 'dj' in mydict else 0)
    output_file = open('output.html', 'w')
    output_file.write(final)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

def main():
  gen_html()


if __name__== "__main__":
  main()