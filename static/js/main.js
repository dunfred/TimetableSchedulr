window.onload = () => {
    const timetable = new Timetable(
        [
            "Mondays",
            "Tuesdays",
            "Wednesdays",
            "Thursday",
            "Friday",
        ],
        [
            "6:30 am - 7:30 am",
            "7:30 am - 8:30 am",
            "8:30 am - 9:30 am",
            "9:30 am - 10:30 am",
            "10:30 am - 11:30 am",
            "11:30 am - 12:30 pm",
            "12:30 pm - 1:30 pm",
            "1:30 pm - 2:30 pm",
            "2:30 pm - 3:30 pm",
            "3:30 pm - 4:30 pm",
            "4:30 pm - 5:30 pm",
            "5:30 pm - 6:30 pm",
        ]
    );

    timetable.onClick = (row_index, cell_index) => {
        const modal = $(".form-overlay");
        if(modal == null) {
            const days = document.querySelector("#add_lecture_form input[name='days']");
            const timings = document.querySelector("#add_lecture_form input[name='timings']");
    
            days.value = timetable.columns[cell_index - 1];
            timings.value = timetable.rows[row_index - 1];
    
            modal.slideDown(600);
        }
    }

    const close_modal = document.querySelector(".close-btn");
    close_modal.addEventListener("click", () => {
        $(".form-overlay").slideUp(500)
    });
}