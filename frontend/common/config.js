const BACKEND_URL = "http://127.0.0.1:8000";

function extract_stations(data) {
    data.forEach(train => {
        stations.add(train.source);
        stations.add(train.destination);
    }
    )
    console.log(stations);
}

function list_bookings(bookings) {
    const container = document.getElementById("bookings_container");
    container.innerHTML = "";
    console.log(bookings)
    bookings.forEach((booking) => {
        train = booking.train;
        const card = document.createElement("div");
        card.className = "col";

        const departure = new Date(train.departure_time).toLocaleString([], {
            month: "short",
            day: "numeric",
            hour: "2-digit",
            minute: "2-digit"
        });

        const arrival = new Date(train.arrival_time).toLocaleString([], {
            month: "short",
            day: "numeric",
            hour: "2-digit",
            minute: "2-digit"
        });

        const bookingDate = new Date(booking.booking_timestamp).toLocaleString();

        card.innerHTML = `
      <div class="card h-100">
        <div class="card-body">
          <h5 class="card-title">${train.name}</h5>
          <h6 class="card-subtitle mb-2 text-muted">${train.source} ➔ ${train.destination}</h6>
          <p class="card-text">
            <strong>PNR:</strong> ${train.pnr}<br>
            <strong>Seat No:</strong> ${booking.seat_number}<br>
            <strong>Departure:</strong> ${departure}<br>
            <strong>Arrival:</strong> ${arrival}<br>
            <button type="button" class="btn btn-success btn-sm w-100 mt-2" id = "cancel-${booking.id}">Cancel Booking</button>
          </p>
        </div>
      </div>
    `;

        container.appendChild(card);
        document.getElementById("cancel-" + booking.id).addEventListener("click", () => {
            cancelBooking(booking.id);
        })
    });
}

function cancelBooking(id) {
    const booking_url = `${BACKEND_URL}/bookings/delete/${id}`;
    fetch(booking_url, {
        method: 'DELETE',
        headers: {
            "Authorization": `token ${localStorage.getItem("token")}`,
        },
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .then(window.location.reload())
}


function list_as_cards(data) {
    const container = document.getElementById("trainContainer");
    container.innerHTML = "";

    data.forEach(train => {
        const col = document.createElement("div");
        col.classname = "col";

        const departureDateTime = new Date(train.departure_time).toLocaleString([], {
            month: "short",
            day: "numeric",
            hour: "2-digit",
            minute: "2-digit"
        });

        const arrivalDateTime = new Date(train.arrival_time).toLocaleString([], {
            month: "short",
            day: "numeric",
            hour: "2-digit",
            minute: "2-digit"
        });

        let button_text;
        if (train.booked_seats === train.total_seats) {
            button_text = "Fully Booked";
        }
        else {
            button_text = "Book Seat (" + (train.total_seats - train.booked_seats) + " Available)";
        }

        col.innerHTML = `
            <div class="card h-100 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">${train.name}</h5>
                    <p class="card-text">
                    <strong>PNR:</strong> ${train.pnr}<br>
                    <strong>From:</strong> ${train.source}<br>
                    <strong>To:</strong> ${train.destination}<br>
                    <strong>Departure:</strong> ${departureDateTime}<br>
                    <strong>Arrival:</strong> ${arrivalDateTime}<br>
                    <button type="submit" class="btn btn-success btn-sm w-100 mt-2" id = "book ${train.id}">${button_text}</button>
                    </p>
                </div>
            </div>
            `;

        container.appendChild(col);
        if (train.booked_seats === train.total_seats) {
            document.getElementById("book " + train.id).disabled = true;
        }
    })

    const bookingModal = new bootstrap.Modal(document.getElementById('bookingModal'));

    if (container.childNodes.length == 0) {
        container.innerHTML = `
        <h2>No train found.</h2>
        `
    }
}

function handleBooking(trainId) {
    const booking_url = `${BACKEND_URL}/bookings/book/`;
    fetch(booking_url, {
        method: 'POST',
        headers: {
            "Authorization": `token ${localStorage.getItem("token")}`,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ "train": trainId })
    })
        .then(response => response.json())
        .then(data => console.log(data));
}

function populateDropdowns(stationsSet) {
    console.log(stationsSet);
    const sourceSelect = document.getElementById("source");
    const destinationSelect = document.getElementById("destination");

    stationsSet.forEach(station => {
        const option = new Option(station, station);
        sourceSelect.add(option.cloneNode(true));
        destinationSelect.add(option);
    });
}

document.addEventListener('click', function (event) {
    if (event.target && event.target.id.startsWith('book')) {
        const trainId = parseInt(event.target.id.split(' ')[1]);
        const train = train_list.find(train => train.id === trainId);

        if (train) {
            const bookingModal = new bootstrap.Modal(document.getElementById('bookingModal'));
            document.getElementById('modal-body-content').innerHTML = `
                <p><strong>Train:</strong> ${train.name}</p>
                <p><strong>PNR:</strong> ${train.pnr}</p>
                <p><strong>From:</strong> ${train.source}</p>
                <p><strong>To:</strong> ${train.destination}</p>
                <p><strong>Seats Available:</strong> ${train.total_seats - train.booked_seats}</p>
            `;
            document.getElementById("confirmBookingBtn").dataset.trainId = trainId;
            bookingModal.show();
        }
    }
});

document.getElementById("confirmBookingBtn").addEventListener("click", function (event) {
    event.preventDefault();
    const trainId = parseInt(this.dataset.trainId);
    handleBooking(trainId);
    const bookingModal = bootstrap.Modal.getInstance(document.getElementById('bookingModal'));
    bookingModal.hide();
    location.reload();
});
