/* login drop down script */
    function toggleDropdown() {
      document.getElementById("loginDropdown").classList.toggle("hidden");
    }

    function toggleMobileMenu() {
      var menu = document.getElementById("mobileMenu");
      if (menu.classList.contains("hidden")) {
        menu.classList.remove("hidden");
        setTimeout(() => {
          menu.style.maxHeight = "500px";
        }, 10);
      } else {
        menu.style.maxHeight = "0px";
        setTimeout(() => {
          menu.classList.add("hidden");
        }, 300);
      }
    }
/*-------------------------------------------------------------------------------------------*/

/*lazy loading */
    document.addEventListener("DOMContentLoaded", function () {
      const landingSection = document.querySelector("#landing-video-section");
      const navbar = document.querySelector("nav");

      setTimeout(() => {
        landingSection.style.transition = "opacity 1s ease-out";
        landingSection.style.opacity = 0;

        setTimeout(() => {
          landingSection.style.display = "none";
          navbar.scrollIntoView({ behavior: "smooth" });
        }, 1000);
      }, 2000);
    });

/*-------------------------------------------------------------------------*/

/*browse books page search bar script*/
    let timeout = null;
    document.getElementById('searchInput').addEventListener('input', function () {
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        document.getElementById('searchForm').submit();
      }, 10000);
    });
    document.getElementById('categorySelect').addEventListener('change', function () {
      document.getElementById('searchForm').submit();
    });

/*---------------------------------------------------------------------*/

/*browse books page modal section page script */

  function openModal(bookId, title, author, category, description, available, coverUrl, pdfUrl) {
    document.getElementById('modalTitle').textContent = title;
    document.getElementById('modalAuthor').textContent = 'by ' + author;
    document.getElementById('modalCategory').textContent = category;
    document.getElementById('modalDescription').textContent = description;

    const availabilityBadge = document.getElementById('modalAvailability');
    if (available === 'True') {
      availabilityBadge.textContent = 'Available';
      availabilityBadge.className = 'bg-green-100 text-green-700 dark:bg-green-700 dark:text-white inline-block text-xs font-semibold px-3 py-1 rounded';
    } else {
      availabilityBadge.textContent = 'Unavailable';
      availabilityBadge.className = 'bg-red-100 text-red-700 dark:bg-red-700 dark:text-white inline-block text-xs font-semibold px-3 py-1 rounded';
    }

    const coverImage = document.getElementById('modalCover');
    if (coverUrl) {
      coverImage.src = coverUrl;
      coverImage.classList.remove('hidden');
    } else {
      coverImage.classList.add('hidden');
    }

    document.getElementById('viewDetailsBtn').href = `/books/book/${bookId}/`;
    const downloadBtn = document.getElementById('downloadBtn');
    if (pdfUrl) {
      downloadBtn.href = pdfUrl;
      downloadBtn.classList.remove('hidden');
    } else {
      downloadBtn.classList.add('hidden');
    }

    document.getElementById('bookModal').classList.remove('hidden');
  }

  function closeModal() {
    document.getElementById('bookModal').classList.add('hidden');
  }

/*----------------------------------------------------------------------------------------*/


/*--------------------------------------------------------------------------------------------*/