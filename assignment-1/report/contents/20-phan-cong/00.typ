#import "@preview/tablex:0.0.5": tablex, hlinex, vlinex, colspanx, rowspanx

#figure(tablex(
  columns: 3,
  align: (horizon, right + horizon, center + horizon),
  auto-vlines: false,
  // map-cells: cell => {
  //   if cell.x == 0 and cell.y > 1 {
  //     cell.content = raw(cell.content.text)
  //   }
  //   cell
  // },
  [*Tên file*],
  [*Số dòng*],
  [*Người review*],
  ..{
    let rows = ()
    let i
    let count
    let name = ""

    for (j, row,) in csv("phan-cong.csv").slice(1).enumerate() {
      rows.push((row.at(0), row.at(1), ()))

      if name == row.at(2) {
        count += 1
        continue
      }

      if i != none {
        rows.at(i).at(2) = rowspanx(count, name)
      }

      name = row.at(2)
      i = j
      count = 1
    }
    rows.at(i).at(2) = rowspanx(count, name)

    rows.flatten()
  },
), caption: "Bảng phân công công việc")
