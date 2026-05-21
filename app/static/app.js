document.addEventListener("DOMContentLoaded", async () => {
  const canvas = document.getElementById("interventionsChart");
  if (!canvas) return;

  const response = await fetch("/api/interventions");
  const chartData = await response.json();

  new Chart(canvas, {
    type: "bar",
    data: chartData,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          labels: {
            color: "#111111"
          }
        }
      },
      scales: {
        x: {
          ticks: { color: "#111111" },
          grid: { color: "#e7e5e4" }
        },
        y: {
          ticks: { color: "#111111" },
          grid: { color: "#e7e5e4" },
          beginAtZero: true
        }
      }
    }
  });
});