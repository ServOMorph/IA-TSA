# Charte Graphique - SéréniaTech

> Guide de style visuel officiel du site web SéréniaTech

---

## Table des matières

1. [Identité visuelle](#1-identité-visuelle)
2. [Palette de couleurs](#2-palette-de-couleurs)
3. [Typographie](#3-typographie)
4. [Espacements](#4-espacements)
5. [Rayons de bordure](#5-rayons-de-bordure)
6. [Ombres](#6-ombres)
7. [Transitions et animations](#7-transitions-et-animations)
8. [Grille et conteneurs](#8-grille-et-conteneurs)
9. [Composants UI](#9-composants-ui)
10. [Mode sombre](#10-mode-sombre)
11. [Accessibilité](#11-accessibilité)
12. [Responsive design](#12-responsive-design)

---

## 1. Identité visuelle

### Logo
- **Fichier principal** : `src/images/logo_optimized.png`
- **Taille navigation** : 50px de hauteur
- **Taille footer** : 150px de largeur
- **Format** : PNG optimisé (~23 KB)

### Slogan
> *"L'innovation au service de votre sérénité numérique"*

### Tonalité
- Moderne et technologique
- Rassurant et humain
- Professionnel mais accessible

---

## 2. Palette de couleurs

### Couleurs principales

| Nom | Variable CSS | Valeur | Aperçu |
|-----|--------------|--------|--------|
| **Primary** | `--color-primary` | `rgb(165, 201, 202)` | ![#A5C9CA](https://via.placeholder.com/20/A5C9CA/A5C9CA) |
| **Primary Dark** | `--color-primary-dark` | `rgb(125, 161, 162)` | ![#7DA1A2](https://via.placeholder.com/20/7DA1A2/7DA1A2) |
| **Primary Light** | `--color-primary-light` | `rgb(185, 221, 222)` | ![#B9DDDE](https://via.placeholder.com/20/B9DDDE/B9DDDE) |
| **Primary Alpha** | `--color-primary-alpha` | `rgba(165, 201, 202, 0.1)` | Transparence 10% |

### Couleurs de texte

| Nom | Variable CSS | Valeur | Contraste | Usage |
|-----|--------------|--------|-----------|-------|
| **Dark** | `--color-dark` | `#000000` | - | Titres principaux |
| **Text** | `--color-text` | `#1a1a1a` | 16:1 | Texte principal |
| **Text Light** | `--color-text-light` | `#2d2d2d` | 13:1 | Texte secondaire |
| **Text Muted** | `--color-text-muted` | `#404040` | 10:1 | Citations, légendes |

### Couleurs de fond

| Nom | Variable CSS | Valeur | Usage |
|-----|--------------|--------|-------|
| **Background** | `--color-bg` | `#ffffff` | Fond principal |
| **Background Alt** | `--color-bg-alt` | `#f7fafc` | Sections alternées |
| **Background Dark** | `--color-bg-dark` | `#edf2f7` | Éléments de contraste |

### Couleurs sémantiques

| Nom | Variable CSS | Valeur | Usage |
|-----|--------------|--------|-------|
| **Success** | `--color-success` | `#48bb78` | Validations, succès |
| **Warning** | `--color-warning` | `#ed8936` | Avertissements |
| **Error** | `--color-error` | `#f56565` | Erreurs |

### Codes hexadécimaux de référence

```css
/* Copier-coller pour design tools */
Primary:        #A5C9CA
Primary Dark:   #7DA1A2
Primary Light:  #B9DDDE
Dark:           #000000
Text:           #1A1A1A
Text Light:     #2D2D2D
Background:     #FFFFFF
Background Alt: #F7FAFC
Success:        #48BB78
Warning:        #ED8936
Error:          #F56565
```

---

## 3. Typographie

### Polices

| Usage | Police | Fallback |
|-------|--------|----------|
| **Corps de texte** | Inter | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif |
| **Titres / Display** | Space Grotesk | Inter, sans-serif |

### Import Google Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
```

### Échelle typographique

| Nom | Variable CSS | Taille | Équivalent px |
|-----|--------------|--------|---------------|
| **xs** | `--text-xs` | 0.75rem | 12px |
| **sm** | `--text-sm` | 0.875rem | 14px |
| **base** | `--text-base` | 1rem | 16px |
| **lg** | `--text-lg` | 1.125rem | 18px |
| **xl** | `--text-xl` | 1.25rem | 20px |
| **2xl** | `--text-2xl` | 1.5rem | 24px |
| **3xl** | `--text-3xl` | 1.875rem | 30px |
| **4xl** | `--text-4xl` | 2.25rem | 36px |
| **5xl** | `--text-5xl` | 3rem | 48px |
| **6xl** | `--text-6xl` | 3.75rem | 60px |

### Hiérarchie des titres

| Élément | Police | Taille | Poids | Interligne |
|---------|--------|--------|-------|------------|
| **h1** | Space Grotesk | 3rem (48px) | 700 | 1.2 |
| **h2** | Space Grotesk | 2.25rem (36px) | 700 | 1.2 |
| **h3** | Space Grotesk | 1.875rem (30px) | 700 | 1.2 |
| **h4** | Space Grotesk | 1.5rem (24px) | 700 | 1.2 |
| **h5** | Space Grotesk | 1.25rem (20px) | 700 | 1.2 |
| **h6** | Space Grotesk | 1.125rem (18px) | 700 | 1.2 |
| **body** | Inter | 1rem (16px) | 400 | 1.6 |

---

## 4. Espacements

### Échelle d'espacement

| Nom | Variable CSS | Valeur | Équivalent px |
|-----|--------------|--------|---------------|
| **xs** | `--space-xs` | 0.25rem | 4px |
| **sm** | `--space-sm` | 0.5rem | 8px |
| **md** | `--space-md` | 1rem | 16px |
| **lg** | `--space-lg` | 1.5rem | 24px |
| **xl** | `--space-xl` | 2rem | 32px |
| **2xl** | `--space-2xl` | 3rem | 48px |
| **3xl** | `--space-3xl` | 4rem | 64px |
| **4xl** | `--space-4xl` | 6rem | 96px |

### Usages recommandés

- **Entre paragraphes** : `--space-md` (16px)
- **Entre sections** : `--space-4xl` (96px)
- **Padding cards** : `--space-xl` (32px)
- **Gap grilles** : `--space-xl` à `--space-2xl`
- **Padding boutons** : `--space-md` vertical, `--space-xl` horizontal

---

## 5. Rayons de bordure

| Nom | Variable CSS | Valeur | Usage |
|-----|--------------|--------|-------|
| **sm** | `--radius-sm` | 0.25rem (4px) | Inputs, focus |
| **md** | `--radius-md` | 0.5rem (8px) | Petits éléments |
| **lg** | `--radius-lg` | 0.75rem (12px) | Icons containers |
| **xl** | `--radius-xl` | 1rem (16px) | Cards |
| **2xl** | `--radius-2xl` | 1.5rem (24px) | Grandes cards |
| **full** | `--radius-full` | 9999px | Boutons, badges |

---

## 6. Ombres

| Nom | Variable CSS | Valeur | Usage |
|-----|--------------|--------|-------|
| **sm** | `--shadow-sm` | `0 1px 2px 0 rgba(0, 0, 0, 0.05)` | Navigation, cards au repos |
| **md** | `--shadow-md` | `0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)` | Boutons hover |
| **lg** | `--shadow-lg` | `0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)` | Cards hover |
| **xl** | `--shadow-xl` | `0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)` | Cards actives, modals |

---

## 7. Transitions et animations

### Durées de transition

| Nom | Variable CSS | Valeur | Usage |
|-----|--------------|--------|-------|
| **Fast** | `--transition-fast` | 150ms | Hover couleurs, focus |
| **Base** | `--transition-base` | 250ms | Hover généraux |
| **Slow** | `--transition-slow` | 350ms | Animations complexes |

### Courbe d'accélération
```css
cubic-bezier(0.4, 0, 0.2, 1)
```

### Animations keyframes

#### fadeInUp (Hero)
```css
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

#### float (Illustrations)
```css
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}
```

#### slideInUp (Cookie banner)
```css
@keyframes slideInUp {
    from { transform: translateY(100%); }
    to { transform: translateY(0); }
}
```

### Respect des préférences utilisateur
```css
@media (prefers-reduced-motion: reduce) {
    /* Désactiver les animations */
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
}
```

---

## 8. Grille et conteneurs

### Largeurs de conteneur

| Nom | Variable CSS | Valeur |
|-----|--------------|--------|
| **sm** | `--container-sm` | 640px |
| **md** | `--container-md` | 768px |
| **lg** | `--container-lg` | 1024px |
| **xl** | `--container-xl` | 1280px |

### Conteneur principal
```css
.container {
    width: 100%;
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 24px; /* Mobile: 24px, Desktop: 48px */
}
```

### Grilles responsives

**Services Grid** :
- Mobile : 1 colonne
- Tablet (768px+) : 2 colonnes
- Desktop (1024px+) : 3 colonnes

**Footer Grid** :
- Mobile : 1 colonne
- Tablet (768px+) : 4 colonnes (1.5fr 1fr 1fr 1fr)

---

## 9. Composants UI

### Boutons

#### Bouton primaire
```css
.btn-primary {
    background-color: rgb(165, 201, 202);
    color: white;
    padding: 16px 32px;
    border-radius: 9999px;
    font-weight: 600;
    font-size: 16px;
}
```

#### Bouton secondaire
```css
.btn-secondary {
    background-color: transparent;
    color: rgb(125, 161, 162);
    border: 2px solid rgb(165, 201, 202);
    padding: 16px 32px;
    border-radius: 9999px;
}
```

#### États des boutons
- **Hover** : translateY(-2px), shadow-lg
- **Focus** : outline 3px solid primary, offset 2px

### Cards

#### Service Card
```css
.service-card {
    background: white;
    padding: 32px;
    border-radius: 16px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    border: 1px solid transparent;
}

/* Hover */
.service-card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-xl);
    border-color: rgb(185, 221, 222);
}
```

#### Testimonial Card
```css
.testimonial-card {
    background: white;
    padding: 32px;
    border-radius: 16px;
    box-shadow: var(--shadow-sm);
    border-left: 4px solid rgb(165, 201, 202);
}
```

### Navigation

- **Position** : Sticky top: 0
- **Background** : rgba(255, 255, 255, 0.95)
- **Effect** : backdrop-filter: blur(10px)
- **Z-index** : 50

### Footer

- **Background** : Gradient linéaire #1a1a1a → #0a0a0a
- **Couleur titres** : Primary Light
- **Couleur texte** : rgba(255, 255, 255, 0.85)

---

## 10. Mode sombre

Le site détecte automatiquement la préférence système via `prefers-color-scheme: dark`.

### Variables mode sombre

| Variable | Mode clair | Mode sombre |
|----------|------------|-------------|
| `--color-dark` | #000000 | #f7fafc |
| `--color-text` | #1a1a1a | #e2e8f0 |
| `--color-text-light` | #2d2d2d | #cbd5e0 |
| `--color-bg` | #ffffff | #1a202c |
| `--color-bg-alt` | #f7fafc | #2d3748 |
| `--color-bg-dark` | #edf2f7 | #4a5568 |

### Éléments spécifiques
- **Navbar** : rgba(26, 32, 44, 0.95)
- **Cards** : var(--color-bg-alt)
- **Footer** : Reste toujours sombre (inchangé)

---

## 11. Accessibilité

### Conformité WCAG 2.1 AA

#### Contraste
- **Texte principal** : Ratio 16:1 minimum
- **Texte secondaire** : Ratio 13:1 minimum
- **Texte muted** : Ratio 10:1 minimum
- **Minimum requis** : 4.5:1 pour texte normal

#### Focus visible
```css
*:focus-visible {
    outline: 3px solid rgb(165, 201, 202);
    outline-offset: 2px;
    border-radius: 4px;
}
```

#### Skip link
- Lien d'évitement en haut de page
- Visible uniquement au focus clavier

#### Attributs ARIA
- Labels sur tous les éléments interactifs
- Roles appropriés sur les sections
- aria-current="page" pour navigation active

#### Navigation clavier
- Tab : navigation forward
- Shift+Tab : navigation backward
- Enter : activer liens
- Espace : activer boutons
- Escape : fermer menu mobile

---

## 12. Responsive design

### Breakpoints

| Nom | Valeur | Description |
|-----|--------|-------------|
| **Mobile** | < 768px | Téléphones |
| **Tablet** | 768px - 1023px | Tablettes |
| **Desktop** | 1024px+ | Ordinateurs |

### Comportements responsifs

#### Typographie
- **Hero title** : 48px → 36px (mobile)
- **Hero subtitle** : 20px → 18px (mobile)
- **Section title** : 36px constant

#### Navigation
- **Desktop** : Menu horizontal inline
- **Mobile** : Menu hamburger, overlay plein écran

#### Grilles
- **Services** : 3 cols → 2 cols → 1 col
- **Témoignages** : 3 cols → 1 col
- **Footer** : 4 cols → 1 col

#### Espacements
- **Hero padding** : 96px → 64px (mobile)
- **Container padding** : 48px → 24px (mobile)
- **CTA buttons** : Inline → Stacked (mobile)

---

## Utilisation des variables CSS

### Exemple d'utilisation

```css
.mon-element {
    /* Couleurs */
    background-color: var(--color-primary);
    color: var(--color-text);

    /* Typographie */
    font-family: var(--font-main);
    font-size: var(--text-lg);

    /* Espacements */
    padding: var(--space-lg) var(--space-xl);
    margin-bottom: var(--space-md);

    /* Bordures */
    border-radius: var(--radius-xl);

    /* Ombres */
    box-shadow: var(--shadow-md);

    /* Transitions */
    transition: all var(--transition-base);
}
```

---

## Fichiers de référence

- **CSS principal** : `src/css/main.css`
- **CSS minifié** : `src/css/main.min.css`
- **Logo** : `src/images/logo_optimized.png`
- **Polices** : Google Fonts (Inter, Space Grotesk)

---

*Document généré le 08/01/2026 - SéréniaTech*
