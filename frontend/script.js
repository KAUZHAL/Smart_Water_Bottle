let waterIntake = 0; // Default intake based on calculation or custom goal

function calculateWaterIntake(event) {
  event.preventDefault();

  const weight = parseFloat(document.getElementById("weight").value);
  const activityLevel = document.getElementById("activity").value;
  const wakeTime = document.getElementById("wakeTime").value;
  const sleepTime = document.getElementById("sleepTime").value;

  // Basic water intake calculation based on weight and activity level
  waterIntake = weight * 0.033; // baseline: 33ml per kg of body weight

  // Adjust intake based on activity level
  if (activityLevel === "light") {
    waterIntake *= 1.1;
  } else if (activityLevel === "moderate") {
    waterIntake *= 1.3;
  } else if (activityLevel === "active") {
    waterIntake *= 1.5;
  }

  // Hide the form
  document.getElementById("waterForm").style.display = "none";

  // Display results
  const result = document.getElementById("result");
  result.innerHTML = `
        <p>Recommended Daily Water Intake:<br> <strong>${waterIntake.toFixed(
          2
        )} liters</strong></p>
        <p>Based on your schedule from <strong>${wakeTime}</strong> to <strong>${sleepTime}</strong>, aim to stay hydrated consistently throughout the day.</p>
    `;
  result.style.display = "block";

  // Show custom goal section
  document.getElementById("customGoalSection").style.display = "block";
}

function setCustomGoal() {
  const customGoal = parseFloat(document.getElementById("customGoal").value);
  if (isNaN(customGoal) || customGoal <= 0) {
    alert("Please enter a valid custom goal.");
    return;
  }

  // Update the result with custom goal
  waterIntake = customGoal; // Set custom water intake goal
  const result = document.getElementById("result");
  result.innerHTML = `
        <p>Your Custom Water Intake Goal: <strong>${waterIntake.toFixed(
          2
        )} liters</strong></p>
        <p>Keep this target in mind as you go about your day.</p>
    `;
}

function finishAndSendData() {
  // Send the water intake data to the backend
  fetch("http://localhost:8000/user_data", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      waterIntake: waterIntake,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      alert("Your data has been successfully submitted!");
      console.log("Server response:", data);
    })
    .catch((error) => {
      alert("There was an error submitting your data.");
      console.error("Error:", error);
    });
}
