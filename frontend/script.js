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
  strDate = currDay.getFullYear() + "-" + currDay.getMonth() + "-" + currDay.getDate()
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
}


function scrollDates(direction) {
    const dateCarousel = document.getElementById('dateCarousel');
    dateCarousel.scrollLeft += direction * 120; // Adjust the scroll distance as needed
  }