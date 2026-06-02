async function analyze() {
  document.getElementById("loading").classList.remove("hidden");

  // Your existing fetch call here

  // After response:
  const data = await response.json();

  document.getElementById("gene").innerText = data.gene;
  document.getElementById("variant").innerText = data.variant;
  document.getElementById("metabolizer").innerText = data.metabolizer;
  document.getElementById("drug").innerText = data.drug;
  document.getElementById("recommendation").innerText = data.recommendation;
  document.getElementById("explanation").innerText = data.explanation;

  const badge = document.getElementById("riskBadge");
  badge.innerText = data.risk;
  badge.className = "risk-badge";

  if (data.risk === "Safe") badge.classList.add("risk-safe");
  else if (data.risk === "Adjust Dosage") badge.classList.add("risk-adjust");
  else if (data.risk === "Toxic") badge.classList.add("risk-toxic");
  else if (data.risk === "Ineffective") badge.classList.add("risk-ineffective");
  else badge.classList.add("risk-unknown");

  document.getElementById("loading").classList.add("hidden");
  document.getElementById("results").classList.remove("hidden");
}

