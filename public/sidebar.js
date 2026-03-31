/**
 * Sidebar Toggle Functionality
 * Collapses/expands the sidebar for better content viewing
 */

(function() {
    'use strict';

    // Initialize sidebar toggle
    function initSidebarToggle() {
        const sidebar = document.querySelector('.sidebar');
        if (!sidebar) return;

        // Create toggle button
        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'sidebar-toggle';
        toggleBtn.innerHTML = '<i class="ph ph-caret-left"></i>';
        toggleBtn.setAttribute('aria-label', 'Toggle sidebar');
        toggleBtn.setAttribute('title', 'Expandir/Recolher menu');

        // Insert toggle button after logo area
        const logoArea = sidebar.querySelector('.logo-area');
        if (logoArea) {
            logoArea.parentNode.insertBefore(toggleBtn, logoArea.nextSibling);
        }

        // Load saved state from localStorage
        const savedState = localStorage.getItem('sidebarCollapsed');
        if (savedState === 'true') {
            sidebar.classList.add('collapsed');
        }

        // Toggle on click
        toggleBtn.addEventListener('click', () => {
            sidebar.classList.toggle('collapsed');
            
            // Save state to localStorage
            const isCollapsed = sidebar.classList.contains('collapsed');
            localStorage.setItem('sidebarCollapsed', isCollapsed);
            
            // Update icon
            const icon = toggleBtn.querySelector('i');
            if (icon) {
                icon.className = isCollapsed ? 'ph ph-caret-right' : 'ph ph-caret-left';
            }
            
            // Dispatch custom event for other components to react
            window.dispatchEvent(new CustomEvent('sidebar:toggle', { 
                detail: { collapsed: isCollapsed } 
            }));
        });
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSidebarToggle);
    } else {
        initSidebarToggle();
    }
})();
