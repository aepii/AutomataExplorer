from flask import Flask, render_template, request, jsonify
  
app = Flask(__name__) 
  
@app.route("/") 
def home(): 
    return render_template(
         "index.html"
    )

@app.route('/', methods=['POST'])
def test_alphabet():
    alphabet = request.form.get('alphabet')

    # Process the data (you can replace this with your logic)
    result = f"Received alphabet: {alphabet}"

    # Send the result back to the front-end
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)