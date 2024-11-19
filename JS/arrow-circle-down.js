import React from 'react';

function ArrowCircleDown({ color = '#1B1B1B' }) {
    return (
        <svg width="auto" height="100%" viewBox="0 0 420 420" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clipPath="url(#clip0_56_1317)">
<path fillRule="evenodd" clipRule="evenodd" d="M61.5071 61.5076C-20.503 143.518 -20.503 276.482 61.5071 358.492C143.517 440.503 276.482 440.503 358.492 358.492C440.502 276.482 440.502 143.518 358.492 61.5076C276.482 -20.5025 143.517 -20.5025 61.5071 61.5076ZM265.407 217.952C273.217 225.763 273.217 238.426 265.407 246.236L222.98 288.663C221.387 290.256 219.591 291.525 217.676 292.468C214.95 293.861 211.862 294.646 208.59 294.646C201.895 294.646 195.969 291.357 192.339 286.306L152.27 246.236C144.459 238.426 144.459 225.763 152.27 217.952C160.08 210.142 172.743 210.142 180.554 217.952L188.59 225.989L188.59 151.01C188.59 139.964 197.545 131.01 208.59 131.01C219.636 131.01 228.59 139.964 228.59 151.01V226.484L237.122 217.952C244.933 210.142 257.596 210.142 265.407 217.952Z" fill={color}/>
</g>
<defs>
<clipPath id="clip0_56_1317">
<rect width="420" height="420" fill="white"/>
</clipPath>
</defs>
</svg>
    );
}

ArrowCircleDown.metadata = { tags: ["directional", "pointer", "pointing", "arrowhead", "arrows", "arrow", "circle", "down"] };

export default ArrowCircleDown;