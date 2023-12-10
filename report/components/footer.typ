#let m = yaml("/metadata.yml")

#set text(font: m.at("fonts").at("monospace"), size: 8pt)
#show: block.with(
  stroke: (top: .25pt),
  inset: (top: 1em),
)

#locate(loc => [
  // skip first page footer
  #if loc.page() == 1 {
    return
  }

  #let current-page = counter(page).at(loc).at(0)
  #let total-pages = counter(page).final(loc).at(0)

  #let semester = m.at("học kỳ")
  #let semester-of-year = calc.rem(semester, 10)
  // change this if you use this in the 2100s
  #let year-from = calc.round(semester / 10) + 2000
  #let year-to = year-from + 1

  #m.at("loại tài liệu") môn #m.at("môn học").at("tên") -
  Học kỳ #semester-of-year năm học #year-from - #year-to
  #h(1fr)
  Trang #current-page/#total-pages
])