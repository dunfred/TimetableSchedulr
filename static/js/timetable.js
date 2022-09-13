class Timetable {

    constructor(columns = [], rows = [], selector = ".timetable table") {
        this.table = document.querySelector(selector);

        this.columns = columns;
        this.rows = rows;

        for(let row_index = 0; row_index < this.table.rows.length; row_index++) {
            let row = this.table.rows[row_index];
            let cells = row.cells;
        
            for (let cell_index = 0; cell_index < cells.length; cell_index++) {
                let cell = cells[cell_index];
        
                cell.addEventListener("click", () => {this.onClick(row_index, cell_index)});
            }
        }
    }


    onClick = (row_index, cell_index) => {}
}



