function scrollDates(direction) {
    const dateCarousel = document.getElementById('dateCarousel');
    dateCarousel.scrollLeft += direction * 120; // Adjust the scroll distance as needed
  }

  document.addEventListener("DOMContentLoaded", function () {
    const dateElements = document.querySelectorAll('.date');
    const eventInfo = document.getElementById('event-info');
    const dateCarousel = document.getElementById('dateCarousel');

    dateElements.forEach(function (dateElement) {
      dateElement.addEventListener('click', function () {
        const selectedDate = dateElement.dataset.date;
  
        
          eventInfo.innerHTML = `<p>Event information for ${selectedDate}<br>  
        Vehicle Type: <br> 
        testing 123</p>`;
        
        
      
        const selectedDateIndex = Array.from(dateElements).indexOf(dateElement);
        const scrollPosition = (selectedDateIndex * 120) - (dateCarousel.clientWidth / 2) + (dateElement.clientWidth / 2);
        dateCarousel.scrollLeft = scrollPosition;
        // 
      });

      
    });
  });