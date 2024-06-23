from flask import Flask, request, render_template_string

app = Flask(__name__)

def generate_groups(n):
    groups = []
    for ai in range(1, n + 1):
        group = []
        for bj in range(n):
            element = ai + bj * (n + 1)
            group.append(element)
        groups.append(group)

    for i in range(1, n):
        for j in range(n - i, n):
            groups[i][j] -= n

    return groups

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            n = int(request.form['number'])
            if n <= 0:
                raise ValueError("Please enter a positive integer.")
            groups = generate_groups(n)
            return render_template_string(template, groups=groups)
        except ValueError as e:
            return render_template_string(template, error=str(e))
    return render_template_string(template)

template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Group Generator</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <style>
      body {
        padding-top: 5rem;
      }
      .container {
        max-width: 600px;
      }
      .result {
        white-space: pre-wrap;
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 5px;
      }
    </style>
  </head>
  <body>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="#">Group Generator</a>
    </nav>
    <main role="main" class="container">
      <div class="text-center mt-5">
        <h1>Group Generator</h1>
        <p class="lead">Enter a positive integer to generate structured groups.</p>
        <form method="post" class="mb-4">
          <div class="form-group">
            <input type="number" class="form-control" id="number" name="number" placeholder="Enter a positive integer" required>
          </div>
          <button type="submit" class="btn btn-primary">Generate</button>
        </form>
        {% if error %}
          <div class="alert alert-danger">{{ error }}</div>
        {% endif %}
        {% if groups %}
          <h2>Generated Groups</h2>
          <div class="result">{{ groups }}</div>
        {% endif %}
      </div>
    </main>
  </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
