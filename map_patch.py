import re

with open('base-martinique.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace CSS
css_pattern = re.compile(r'        /\* === Carte stratégique \(premium émotionnel\) === \*/.*?(?=        </style>)', re.DOTALL)
new_css = """        /* === Carte stratégique intégrée === */
        .map-section {
            background-color: var(--white);
            padding: 80px 10%;
            border-top: 1px solid rgba(0,0,0,0.03);
            border-bottom: 1px solid rgba(0,0,0,0.03);
        }

        .map-card {
            margin: 0 auto;
            max-width: 1100px;
        }

        .map-card__header {
            text-align: center;
            margin-bottom: 50px;
        }

        .map-card__header h2 {
            font-size: 2.8rem;
            color: var(--text-main);
            margin-bottom: 15px;
        }

        .map-card__header p {
            font-size: 1.15rem;
            color: var(--text-muted);
            font-weight: 300;
        }

        .map-frame {
            border-radius: 8px;
            overflow: hidden;
            background-color: var(--bg-secondary);
            border: 1px solid rgba(0,0,0,0.04);
            box-shadow: 0 10px 40px rgba(0,0,0,0.02);
            position: relative;
        }

        .caribbean-map {
            display: block;
            width: 100%;
            height: auto;
        }

        .caribbean-map .ocean {
            fill: transparent;
        }

        .caribbean-map .rings circle {
            fill: none;
            stroke: rgba(0,0,0,0.04);
            stroke-width: 1;
            stroke-dasharray: 4 8;
        }

        .caribbean-map .island {
            fill: #EAE6DF;
            stroke: #DCD8D0;
            stroke-width: 1;
        }

        .caribbean-map .routes .route {
            fill: none;
            stroke: var(--accent);
            stroke-width: 1.5;
            stroke-linecap: round;
            stroke-dasharray: 4 12;
        }

        .caribbean-map .hubDot {
            fill: var(--accent);
            opacity: 0.9;
        }

        .caribbean-map .hubHalo {
            fill: none;
            stroke: var(--accent);
            stroke-width: 2;
        }

        .caribbean-map .labels .place {
            fill: var(--text-muted);
            font-size: 13px;
            font-weight: 500;
        }

        .caribbean-map .labels .placeEm {
            fill: var(--accent);
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .caribbean-map .labels .tagBg {
            fill: var(--white);
            stroke: rgba(0,0,0,0.05);
            stroke-width: 1;
        }

        .caribbean-map .labels .tagTitle {
            fill: var(--text-main);
            font-size: 14px;
            font-weight: 600;
        }

        .caribbean-map .labels .tagSub {
            fill: var(--text-muted);
            font-size: 12px;
        }

        .map-card__footer {
            margin-top: 25px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
            padding: 0 10px;
        }

        .map-bullets {
            display: flex;
            gap: 20px;
            font-size: 0.9rem;
            color: var(--text-main);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .map-bullets span {
            display: flex;
            align-items: center;
        }
        
        .map-bullets span::before {
            content: "•";
            color: var(--accent);
            margin-right: 8px;
            font-size: 1.2rem;
        }

        .map-note {
            color: var(--text-muted);
            font-size: 0.85rem;
            font-weight: 300;
        }

        /* --- Micro-animations --- */
        @media (prefers-reduced-motion: reduce) {
            .caribbean-map .routes .route,
            .caribbean-map .hubHalo,
            .caribbean-map .hubDot {
                animation: none !important;
            }
        }

        .caribbean-map .routes .route {
            stroke-dasharray: 4 12;
            animation: routeDraw 6.8s linear infinite;
            animation-delay: var(--d, 0s);
        }

        .caribbean-map .routes .route:nth-child(1) { --d: 0.0s; }
        .caribbean-map .routes .route:nth-child(2) { --d: 0.7s; }
        .caribbean-map .routes .route:nth-child(3) { --d: 1.3s; }
        .caribbean-map .routes .route:nth-child(4) { --d: 1.9s; }
        .caribbean-map .routes .route:nth-child(5) { --d: 2.5s; }

        @keyframes routeDraw {
            0% { stroke-dashoffset: 0; opacity: 0.4; }
            50% { stroke-dashoffset: -100; opacity: 0.8; }
            100% { stroke-dashoffset: -200; opacity: 0.4; }
        }

        .caribbean-map .hubHalo {
            transform-origin: 510px 300px;
            animation: haloPulse 3.6s ease-in-out infinite;
            opacity: 0.5;
        }

        @keyframes haloPulse {
            0% { transform: scale(1); opacity: 0.3; }
            50% { transform: scale(1.15); opacity: 0.7; }
            100% { transform: scale(1); opacity: 0.3; }
        }
"""
html = css_pattern.sub(new_css, html)

# Replace SVG Map section
map_pattern = re.compile(r'        <section class="map-card" aria-label="Carte stratégique centrée sur la Martinique">.*?</section>\n    </section>', re.DOTALL)
new_map = """    </section>

    <section class="map-section">
        <div class="map-card" aria-label="Carte stratégique centrée sur la Martinique">
            <div class="map-card__header">
                <h2>Une position idéale pour naviguer</h2>
                <p>Martinique comme point d’ancrage — une lecture claire et progressive des bassins des Caraïbes Sud.</p>
            </div>

            <div class="map-frame" role="img" aria-label="Carte stylisée des Petites Antilles centrée sur la Martinique">
                <svg class="caribbean-map" viewBox="0 0 1000 560" xmlns="http://www.w3.org/2000/svg">
                    <!-- Background -->
                    <defs>
                        <radialGradient id="oceanGlow" cx="50%" cy="45%" r="70%">
                            <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.8" />
                            <stop offset="60%" stop-color="#FFFFFF" stop-opacity="0.1" />
                            <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0" />
                        </radialGradient>

                        <filter id="softShadow" x="-30%" y="-30%" width="160%" height="160%">
                            <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.04" />
                        </filter>
                    </defs>

                    <rect x="0" y="0" width="1000" height="560" rx="0" ry="0" class="ocean" />
                    <rect x="0" y="0" width="1000" height="560" rx="0" ry="0" fill="url(#oceanGlow)" />

                    <!-- Navigation rings (subtle) -->
                    <g class="rings">
                        <circle cx="510" cy="300" r="100" />
                        <circle cx="510" cy="300" r="180" />
                        <circle cx="510" cy="300" r="260" />
                    </g>

                    <!-- Islands (stylized, realistic shapes) -->
                    <g class="islands" filter="url(#softShadow)">
                        <!-- Guadeloupe -->
                        <path d="M 470 130 C 480 120, 495 130, 490 150 C 485 165, 470 160, 465 145 Z" class="island" />
                        <path d="M 490 135 C 505 125, 520 135, 510 150 C 495 155, 485 145, 490 135 Z" class="island" />
                        <circle cx="510" cy="165" r="5" class="island" />

                        <!-- Dominica -->
                        <path d="M 495 190 C 515 180, 525 200, 510 220 C 495 210, 485 195, 495 190 Z" class="island" />

                        <!-- Martinique (encompassing 510,300) -->
                        <path d="M 495 260 C 515 250, 530 270, 520 290 C 525 305, 510 315, 500 305 C 490 300, 485 285, 490 275 Z" class="island" />

                        <!-- Saint Lucia -->
                        <path d="M 515 330 C 530 325, 540 345, 520 365 C 505 355, 505 340, 515 330 Z" class="island" />

                        <!-- Saint Vincent -->
                        <path d="M 540 395 C 555 385, 565 405, 550 420 C 535 410, 535 400, 540 395 Z" class="island" />

                        <!-- Grenadines & Grenada -->
                        <circle cx="560" cy="435" r="3" class="island" />
                        <circle cx="570" cy="450" r="3.5" class="island" />
                        <circle cx="585" cy="465" r="4" class="island" />
                        <circle cx="595" cy="485" r="4" class="island" />
                        <path d="M 605 510 C 620 500, 630 520, 615 535 C 600 525, 600 515, 605 510 Z" class="island" />
                    </g>

                    <!-- Routes (thin, premium) -->
                    <g class="routes">
                        <path d="M510 300 Q 520 260 505 220" class="route" /> <!-- Dominica -->
                        <path d="M505 220 Q 480 180 500 160" class="route" /> <!-- Guadeloupe -->
                        <path d="M510 300 Q 535 320 520 340" class="route" /> <!-- Saint Lucia -->
                        <path d="M510 300 Q 545 345 545 390" class="route" /> <!-- Saint Vincent -->
                        <path d="M545 390 Q 570 440 605 510" class="route" /> <!-- Grenadines -> Grenada -->
                    </g>

                    <!-- Martinique hub marker -->
                    <g class="hub">
                        <circle cx="510" cy="300" r="14" class="hubHalo" />
                        <circle cx="510" cy="300" r="6" class="hubDot" />
                    </g>

                    <!-- Labels -->
                    <g class="labels">
                        <g class="tag" filter="url(#softShadow)">
                            <rect x="70" y="70" width="280" height="64" rx="8" class="tagBg" />
                            <text x="95" y="98" class="tagTitle">Le Marin, Martinique</text>
                            <text x="95" y="118" class="tagSub">Hub opérationnel des Caraïbes Sud</text>
                        </g>

                        <!-- Island labels -->
                        <text x="395" y="145" class="place">Guadeloupe</text>
                        <text x="535" y="210" class="place">Dominique</text>
                        <text x="390" y="285" class="placeEm">Martinique</text>
                        <text x="540" y="340" class="place">Sainte-Lucie</text>
                        <text x="575" y="405" class="place">Saint-Vincent</text>
                        <text x="635" y="525" class="place">Grenade & Grenadines</text>
                    </g>
                </svg>
            </div>

            <div class="map-card__footer">
                <div class="map-bullets" aria-label="Atouts de la base">
                    <span>Protégé</span>
                    <span>Accessible</span>
                    <span>Professionnel</span>
                </div>
                <div class="map-note">Illustration de nos routes de navigation privilégiées.</div>
            </div>
        </div>"""
html = map_pattern.sub(new_map, html)

# Remove the old split-section map
old_map_pattern = re.compile(r'    <section class="split-section">\s*<div class="split-image"></div>\s*<div class="split-content">\s*<h2>Une position idéale pour naviguer</h2>\s*<p>Depuis la Martinique, les routes nautiques s’ouvrent naturellement vers les plus beaux bassins de\s*navigation\..*?</div>\s*</section>\s*', re.DOTALL)
html = old_map_pattern.sub('', html)

with open('base-martinique.html', 'w', encoding='utf-8') as f:
    f.write(html)
