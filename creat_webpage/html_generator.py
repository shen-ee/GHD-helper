import webbrowser
import os

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
            <td>{num_petet}</td>
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
  final = html.format(img_name="img/demo.png",
                      num_bruno=1,
                      num_compy=2,
                      num_tina=3,
                      num_petet=4,
                      num_teleport=1,
                      num_tesla=2,
                      num_laser=3,
                      num_dj=4)
  output_file = open('output.html', 'w')
  output_file.write(final)
  output_file.close()
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2)

def main():
  gen_html()


if __name__== "__main__":
  main()