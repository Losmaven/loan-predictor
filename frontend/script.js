// frontend/script.js
async function makePrediction() {
  const sampleInput = {
    Gender: "Male",
    Married: "Yes",
    Dependents: "1",
    Education: "Graduate",
    Self_Employed: "No",
    ApplicantIncome: 5000,
    CoapplicantIncome: 1500,
    LoanAmount: 200,
    Loan_Amount_Term: 360,
    Credit_History: 1,
    Property_Area: "Urban"
  };

  const response = await fetch("http://127.0.0.1:5000/api/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(sampleInput)
  });

  const result = await response.json();
  document.getElementById("prediction").innerText = `Prediction: ${result.prediction}`;
}
