const markdownSpans = document.getElementsByClassName('markdown-span');

for (let span of markdownSpans) {
  span.innerHTML = marked.parse(span.textContent);
}