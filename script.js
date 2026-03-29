const API = "http://127.0.0.1:8000";


async function calculateFIRE() {
    const income = +incomeEl().value;
    const expenses = +expensesEl().value;
    const goal = +goalEl().value;

    const res = await fetch(API + "/fire", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            age: 25,
            income,
            expenses,
            savings: 0,
            goal_amount: goal
        })
    });

    const data = await res.json();
    fireResult.innerText = `🔥 ${data.years_to_goal} yrs | SIP ₹${data.recommended_sip}`;
}

let chart;

async function calculateHealth() {
    const res = await fetch(API + "/health", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            income: +hIncome.value,
            expenses: +hExpenses.value,
            savings: +hSavings.value,
            debt: +hDebt.value,
            insurance: +hInsurance.value
        })
    });

    const data = await res.json();

    healthResult.innerText = `Score: ${data.score} | ${data.status}`;

    const labels = Object.keys(data.breakdown);
    const values = Object.values(data.breakdown);

    if (chart) chart.destroy();

    const ctx = document.getElementById("healthChart");

    chart = new Chart(ctx, {
        type: "radar",
        data: {
            labels: labels,
            datasets: [{
                label: "Financial Health",
                data: values
            }]
        }
    });
}
async function getAdvice() {
    const event = document.getElementById("event").value;
    const amount = document.getElementById("amount").value;

    const res = await fetch(API + "/life", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            event: event,
            amount: parseFloat(amount)
        })
    });

    const data = await res.json();

    console.log(data); // debug

    document.getElementById("lifeResult").innerText = data.advice;
}

async function lifeAdvisor() {
    const res = await fetch(API + "/life", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            event: event.value,
            amount: +eventAmount.value
        })
    });

    const data = await res.json();
    result.innerText = data.advice;
}

// TAX
async function calculateTax() {
    const income = +salary.value;

    const res = await fetch(API + "/tax", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({income})
    });

    const data = await res.json();
    taxResult.innerText = `Tax: ₹${data.tax}`;
}

// COUPLE
async function couplePlan() {
    const res = await fetch(API + "/couple", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            income1: +p1.value,
            income2: +p2.value,
            expenses: +exp.value,
            savings: 0
        })
    });

    const data = await res.json();
    coupleResult.innerText = `Savings ₹${data.monthly_savings}`;
}

async function askAI() {
    const msg = chatInput.value;

    const res = await fetch(API + "/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ message: msg })
    });

    const data = await res.json();
    chatResult.innerText = data.response;
}   

// MF
async function mfXray() {
    const res = await fetch(API + "/mf", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            invested: +invested.value,
            current: +current.value,
            years: +years.value
        })
    });

    const data = await res.json();
    mfResult.innerText = `XIRR: ${data.xirr}%`;
}

// helpers
const incomeEl = () => document.getElementById("income");
const expensesEl = () => document.getElementById("expenses");
const goalEl = () => document.getElementById("goal");