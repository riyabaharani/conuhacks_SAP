async function getData(date) {
  let response = await fetch("http://localhost:5000/users")
  let res = await response.json()
  fillTable(res,date)
}
getData("2022-10-01");

months = {
  10:"Oct",
  11:"Nov"
}

const firstDay = new Date(2022,10,1)
currDay = firstDay
dateCarousel = document.getElementById("dateCarousel")
for (let i = 1; i <= 60; i++){
  el = document.createElement("div")
  el.classList.add("date")
  el.setAttribute('onclick','scrollOnSelect(event)')
  if (i == 1){el.classList.add("active")}
  strDate = currDay.getFullYear() + "-" + currDay.getMonth() + "-"
  if (i < 10) {
    strDate += "0"
  }
  strDate += currDay.getDate()
  el.setAttribute("data-date",strDate)
  el.setAttribute("value", strDate)
  el.innerHTML = months[currDay.getMonth()] + " " + currDay.getDate()
  dateCarousel.appendChild(el)
  currDay.setDate(firstDay.getDate() + 1)
}

function removeActive(dateElements){
  dateElements.forEach(el => {
    el.classList.remove('active')
  })
}

function scrollOnSelect(e){
  const dateElements = document.querySelectorAll('.date')
  removeActive(dateElements)
  dateElement = e.target
  dateElement.classList.toggle('active')
  document.querySelector('#dateSelected').textContent = dateElement.getAttribute('data-date')
  const dateCarousel = document.getElementById('dateCarousel');
  const selectedDateIndex = Array.from(dateElements).indexOf(dateElement)
  const scrollPosition = (selectedDateIndex * 100) - (dateCarousel.clientWidth / 2) + (dateElement.clientWidth / 2);
  dateCarousel.scrollLeft = scrollPosition
  getData(dateElement.getAttribute('data-date'));
}

function fillTable(data, date) {
  const d = data[date]
  document.querySelector("#compactServed").innerHTML = d["cars_served"]["compact"]
  document.querySelector("#mediumServed").innerHTML = d["cars_served"]["medium"]
  document.querySelector("#fullServed").innerHTML = d["cars_served"]["full-size"]
  document.querySelector("#oneServed").innerHTML = d["cars_served"]["class 1 truck"]
  document.querySelector("#twoServed").innerHTML = d["cars_served"]["class 2 truck"]
  document.querySelector("#compactDeclined").innerHTML = d["turned_away"]["compact"]
  document.querySelector("#mediumDeclined").innerHTML = d["turned_away"]["medium"]
  document.querySelector("#fullDeclined").innerHTML = d["turned_away"]["full-size"]
  document.querySelector("#oneDeclined").innerHTML = d["turned_away"]["class 1 truck"]
  document.querySelector("#twoDeclined").innerHTML = d["turned_away"]["class 2 truck"]
  document.querySelector("#moneyGained").innerHTML = d["money_made"] 
  document.querySelector("#moneyLost").innerHTML = d["money_lost"]
  document.querySelector("#actualRevenue").innerHTML = data["revenue"]
  document.querySelector("#lostRevenue").innerHTML = data["loss"]
  const total = Math.round(d["money_lost"]*360/(d["money_made"] + d["money_lost"]))
  document.querySelector(".pie").style.backgroundImage = `conic-gradient(rgb(249, 38, 115) ${total}deg, rgb(62, 222, 110) ${total}deg)`
}

function scrollDates(direction) {
    const dateCarousel = document.getElementById('dateCarousel');
    dateCarousel.scrollLeft += direction * 120; // Adjust the scroll distance as needed
}

