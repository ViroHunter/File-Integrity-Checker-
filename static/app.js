// File Integrity Checker - Frontend JavaScript
// Handles drag & drop, file selection display, and UX enhancements

(function() {
  'use strict';

  // DOM Elements
  const uploadZone = document.getElementById('uploadZone');
  const fileInput = document.getElementById('fileInput');
  const fileNameDisplay = document.getElementById('fileName');
  const uploadForm = document.getElementById('uploadForm');

  // Prevent default drag behaviors
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    uploadZone.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
  });

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  // Highlight upload zone when dragging over
  ['dragenter', 'dragover'].forEach(eventName => {
    uploadZone.addEventListener(eventName, highlight, false);
  });

  ['dragleave', 'drop'].forEach(eventName => {
    uploadZone.addEventListener(eventName, unhighlight, false);
  });

  function highlight() {
    uploadZone.classList.add('drag-over');
  }

  function unhighlight() {
    uploadZone.classList.remove('drag-over');
  }

  // Handle drop
  uploadZone.addEventListener('drop', handleDrop, false);

  function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;

    if (files.length > 0) {
      fileInput.files = files;
      displayFileName(files[0].name);
    }
  }

  // Handle file selection via browse
  fileInput.addEventListener('change', function() {
    if (this.files && this.files.length > 0) {
      displayFileName(this.files[0].name);
    }
  });

  // Display selected file name
  function displayFileName(name) {
    if (name) {
      fileNameDisplay.textContent = name;
      fileNameDisplay.style.display = 'inline-block';
    } else {
      fileNameDisplay.textContent = '';
      fileNameDisplay.style.display = 'none';
    }
  }

  // Form submission handler (optional - for loading state)
  uploadForm.addEventListener('submit', function(e) {
    const buttons = uploadForm.querySelectorAll('.btn');
    buttons.forEach(btn => {
      btn.disabled = true;
      const originalText = btn.innerHTML;
      btn.innerHTML = '<span>Processing...</span>';

      // Re-enable after response (or timeout as fallback)
      setTimeout(() => {
        btn.disabled = false;
        btn.innerHTML = originalText;
      }, 5000);
    });
  });

  // Check if there's a status message on page load and show it
  const statusSection = document.querySelector('.status-section[style*="display: none"]');
  if (statusSection) {
    // This section is handled by Flask template rendering
    // JavaScript status display is for client-side updates only
  }

  // Keyboard accessibility for upload zone
  uploadZone.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      fileInput.click();
    }
  });

  // Add tabindex for keyboard navigation
  uploadZone.setAttribute('tabindex', '0');
  uploadZone.setAttribute('role', 'button');
  uploadZone.setAttribute('aria-label', 'Click or drag file to upload');

})();
