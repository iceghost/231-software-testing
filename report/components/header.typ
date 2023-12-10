#let m = yaml("/metadata.yml")

#set text(font: m.at("fonts").at("monospace"), size: 10pt)
#set par(leading: 0.75em)
#show: block.with(stroke: (bottom: .25pt), inset: (bottom: 1em))
#show: upper

#locate(loc => [
  // skip first page header
  #if loc.page() == 1 {
    return
  }

  #h(0.2cm)
  #box(image("/components/logo.png", height: 2.2em))
  #h(0.1cm)
  #box[
    Trường Đại học Bách Khoa - ĐHQG-HCM \
    Khoa Khoa học và Kỹ thuật Máy tính
  ]
  #h(1fr)
])