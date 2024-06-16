document.addEventListener('DOMContentLoaded', () => {
  const userContainer = document.getElementById('userContainer');
  let lastScrollTop = 0;
  let hideTimeout;

  function handleScroll() {
    const scrollTop = userContainer.scrollTop;
    const scrollHeight = userContainer.scrollHeight;
    const offsetHeight = userContainer.offsetHeight;
    const scrollBottom = scrollHeight - offsetHeight - scrollTop;

    if (hideTimeout) {
      clearTimeout(hideTimeout);
    }

    if (scrollTop < 10 || scrollBottom < 10) {
      hideScrollbar();
    } else {
      showScrollbar();
    }

    lastScrollTop = scrollTop;
  }

  function hideScrollbar() {
    userContainer.classList.add('hide-scrollbar');
  }

  function showScrollbar() {
    userContainer.classList.remove('hide-scrollbar');
  }

  userContainer.addEventListener('scroll', () => {
    handleScroll();

    hideTimeout = setTimeout(() => {
      if (userContainer.scrollTop === lastScrollTop) {
        hideScrollbar();
      }
    }, 500);
  });

  const scrollTop = userContainer.scrollTop;
  const scrollHeight = userContainer.scrollHeight;
  const offsetHeight = userContainer.offsetHeight;
  const scrollBottom = scrollHeight - offsetHeight - scrollTop;

  if (scrollTop < 10 || scrollBottom < 10) {
    hideScrollbar();
  } else {
    showScrollbar();
  }
});
