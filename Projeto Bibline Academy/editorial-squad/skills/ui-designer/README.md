# 🖼️ UI Designer Agent - Documentação Completa

**Especialista em Design Systems Premium e Interfaces Responsivas**

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | UI Designer |
| **Tipo** | Designer UI Senior |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |

---

## Objetivo

Transformar conceitos de design em sistemas visuais coesos, escaláveis e premium. Domina design responsivo, accessibility (WCAG), sistemas de design tokenizados e componentização.

---

## Comandos

### **1. `/ui-designer create-system <nome>`**

**Descrição:** Cria design system completo.

**Sintaxe:**
```bash
/ui-designer create-system <nome>
```

**Exemplo:**
```bash
/ui-designer create-system "Bibline Vision Board

Co-authored-by: Qwen-Coder <qwen-coder@alibabacloud.com>"
```

**Saída:**
```markdown
# 🎨 Design System — Bibline Vision Board

## 1. Sistema de Tokens

### Colors
```
primary: {
  50: #eff6ff
  100: #dbeafe
  500: #3b82f6  # Main
  600: #2563eb
  700: #1d4ed8
}

semantic: {
  success: #10b981
  warning: #f59e0b
  danger: #ef4444
  info: #06b6d4
}
```

### Typography
```
font-family: 'Outfit', sans-serif
scale: 12, 14, 16, 18, 20, 24, 32, 48, 64
line-heights: 1.25, 1.5, 1.625
weights: 300, 400, 500, 600, 700
```

### Spacing
```
base: 8px
units: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64
```

### Shadows
```
sm: 0 1px 2px rgba(0,0,0,0.05)
md: 0 4px 6px rgba(0,0,0,0.1)
lg: 0 10px 15px rgba(0,0,0,0.1)
xl: 0 20px 25px rgba(0,0,0,0.15)
```

### Breakpoints
```
xs: 320px   # Mobile small
sm: 480px   # Mobile large
md: 768px   # Tablet
lg: 1024px  # Desktop
xl: 1280px  # Desktop large
xxl: 1536px # Extra large
```

## 2. Componentes

### Atoms
- Buttons (primary, secondary, outline)
- Inputs (text, select, checkbox)
- Labels
- Icons

### Molecules
- Cards (KPI, discipline)
- Forms (search, filter)
- Navigation items

### Organisms
- Header
- Footer
- Sidebar
- KPI Grid

## 3. Accessibility

- ✅ WCAG AA contrast ratios
- ✅ Keyboard navigation
- ✅ Screen reader support
- ✅ Focus indicators
```

---

### **2. `/ui-designer create-component <nome>`**

**Descrição:** Cria componente específico.

**Sintaxe:**
```bash
/ui-designer create-component <nome>
```

**Exemplo:**
```bash
/ui-designer create-component "KPI Card"
```

**Saída:**
```markdown
# 🧩 Componente — KPI Card

## Props
```typescript
interface KPICardProps {
  title: string
  value: number | string
  icon: string
  color: 'blue' | 'green' | 'orange' | 'red'
  trend?: 'up' | 'down' | 'neutral'
}
```

## Variants
- **Default:** Card simples
- **With Trend:** Inclui indicador de tendência
- **Compact:** Versão reduzida

## Responsive
- **Mobile:** Stack vertical
- **Tablet:** 2 columns
- **Desktop:** 4 columns

## Accessibility
- Role: `article`
- Aria-label: `title`
- Focus: outline 2px
```

---

### **3. `/ui-designer apply-theme <tema>`**

**Descrição:** Aplica tema visual.

**Sintaxe:**
```bash
/ui-designer apply-theme <tema>
```

**Exemplo:**
```bash
/ui-designer apply-theme "Dark Mode"
```

---

## Atribuições Principais

### **1. Design System Premium**

#### Sistema de Tokens
```
tokens/
├── colors/
│   ├── primary/
│   ├── secondary/
│   ├── semantic/
│   ├── neutral/
│   └── accent/
├── typography/
│   ├── font-families/
│   ├── font-weights/
│   ├── font-sizes/
│   ├── line-heights/
│   └── letter-spacings/
├── spacing/
│   └── base-units/
├── shadows/
│   └── elevation/
├── borders/
│   └── radii/
└── breakpoints/
```

#### Paleta de Cores
- **Hex, RGB, HSL** para cada cor
- **Variantes:** light, dark, muted
- **Contraste:** WCAG AA/AAA
- **Gradientes:** direção e cores

#### Tipografia
- **Font families:** primary, secondary, monospace
- **Type scale:** 12, 14, 16, 18, 20, 24, 32, 48, 64
- **Line heights:** para cada tamanho
- **Font weights:** Regular, Medium, SemiBold, Bold
- **Letter spacing:** tracking

---

### **2. Design Responsivo (Mobile-First)**

#### Breakpoints
```typescript
breakpoints: {
  xs: '320px',   // Mobile small
  sm: '480px',   // Mobile large
  md: '768px',   // Tablet
  lg: '1024px',  // Desktop
  xl: '1280px',  // Desktop large
  xxl: '1536px'  // Extra large
}
```

#### Grid System
- **Container:** Max-width responsivo
- **Columns:** 12-column grid
- **Gutters:** Espaçamento entre colunas
- **Margins:** Margens laterais

#### Componentes Responsivos
Cada componente tem:
- **Mobile:** Layout vertical, touch-friendly (min 44px)
- **Tablet:** Layout adaptativo
- **Desktop:** Layout horizontal completo

---

### **3. Componentização (Atomic Design)**

#### Atoms
- Botões
- Inputs
- Labels
- Ícones

#### Molecules
- Cards
- Forms
- Search bars

#### Organisms
- Headers
- Footers
- Sidebars

#### Templates
- Page layouts

#### Pages
- Páginas completas

---

## Casos de Uso

### **1. Criar Novo Produto**

```bash
@ui-designer "Criar design system para Vision Board"
```

**Processo:**
1. Definir tokens
2. Criar paleta de cores
3. Especificar tipografia
4. Componentizar atoms
5. Criar molecules
6. Montar organisms
7. Documentar

---

### **2. Criar Componente Específico**

```bash
@ui-designer "Criar sidebar responsiva"
```

**Saída:**
```markdown
# 🧩 Sidebar Component

## Props
```typescript
interface SidebarProps {
  items: NavItem[]
  collapsed: boolean
  onToggle: () => void
}
```

## Responsive
- **Desktop:** 280px width, expanded
- **Tablet:** 240px width
- **Mobile:** Collapsed (60px), overlay

## Accessibility
- Role: `navigation`
- Aria-label: "Main navigation"
- Keyboard: Tab, Enter, Escape
```

---

### **3. Aplicar Tema**

```bash
@ui-designer "Aplicar dark mode"
```

**Saída:**
```markdown
# 🌙 Dark Mode Applied

## Color Changes
- Background: #0f172a (was #ffffff)
- Surface: #1e293b (was #f8fafc)
- Text: #f8fafc (was #0f172a)
- Border: rgba(255,255,255,0.1) (was rgba(0,0,0,0.1))

## Contrast Validated
- ✅ All text meets WCAG AA
- ✅ Icons visible on dark background
- ✅ Focus indicators enhanced
```

---

## Links

- [Skill](SKILL.md)
- [Design Thinking](../design-thinking/) (para pesquisa)
- [Vision Board](../../knowledge-base/)
