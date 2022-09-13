window.onload = () => {
    const timetable = new Timetable();

    timetable.onClick = (row_index, cell_index) => {
        console.log(row_index, cell_index);
        console.log(timetable);
    }
}