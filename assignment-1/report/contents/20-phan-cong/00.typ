#import "@preview/tablex:0.0.5": tablex, hlinex, vlinex, colspanx, rowspanx

#show: align.with(center + horizon)

#figure(tablex(
  columns: 3,
  align: (horizon, right + horizon, center + horizon),
  auto-vlines: false,
  map-cells: cell => {
    if cell.x == 0 and cell.y > 0 {
      cell.content = raw(cell.content.text)
    }
    cell
  },
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

#v(2em)

#figure(tablex(
  columns: 2,
  align: (center + horizon, center + horizon),
  auto-vlines: false,
  [*Người review*],
  [*Số dòng*],
  ..{
    let counts = (:)
    for (_, loc, name) in csv("phan-cong.csv").slice(1) {
      let sum = counts.at(name, default: -1)
      if sum == -1 {
        counts.insert(name, int(loc))
      } else {
        counts.insert(name, sum + int(loc))
      }
    }
    counts.pairs().flatten()
  },
), caption: "Tổng số lượng dòng của mỗi thành viên")
