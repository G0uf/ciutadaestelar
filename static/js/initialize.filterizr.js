$(function() {
    setTimeout(function() {
        filterizr();
    }, 500);
});

function filterizr() {
    var options = {
        animationDuration: 0.15,
        filter: 'all',
        callbacks: {
            onFilteringStart: function() {},
            onFilteringEnd: function() {},
            onShufflingStart: function() {},
            onShufflingEnd: function() {},
            onSortingStart: function() {},
            onSortingEnd: function() {}
        },
        delay: 0,
        delayMode: 'alternate',
        easing: 'ease-out',
        filterOutCss: {
            opacity: 0,
            transform: 'scale(1)'
        },
        filterInCss: {
            opacity: 1,
            transform: 'scale(1)'
        },
        layout: 'sameSize',
        selector: '.filtr-container',
        setupControls: true
    };
    var filterizd = $('.filtr-container').filterizr(options);
    filterizd.filterizr('setOptions', options);
}