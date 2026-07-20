# Peeps — Local People Tracker

## Overview
A local fullstack app for keeping track of people in your life — birthdays, notes, contact info. Data is stored as individual markdown files in a `/peeps/` data directory. The React frontend reads and displays these as cards in a clean UI. Built with React + Vite + TypeScript + shadcn/ui + Tailwind CSS v3.

## Architecture
- **Frontend:** React 18 + Vite + TypeScript + shadcn/ui + Tailwind CSS v3
- **Backend:** Express.js API server (runs locally alongside Vite dev server)
- **Data Storage:** Each person is a `.md` file in a `/data/peeps/` directory
- **No database.** Files are the source of truth.

## Markdown File Format
Each person is stored as a markdown file: `/data/peeps/{slug}.md`

Example (`data/peeps/john-doe.md`):
```markdown
---
name: John Doe
birthday: 1990-03-15
phone: 555-123-4567
email: john@example.com
tags: [friend, college]
created: 2026-02-15
---

Met John at college orientation in 2012. Works at a startup downtown.

Always brings the best snacks to game nights. Loves hiking and photography.

Reminder: He's allergic to shellfish — important for dinner plans.
```

The frontmatter contains structured data. The body is freeform notes.

---

## Tasks

### Task 1: Backend API Server
Set up an Express.js server that runs on port 3001 alongside the Vite dev server.

**Endpoints:**
- `GET /api/peeps` — List all people (parse frontmatter from all .md files, return as JSON array)
- `GET /api/peeps/:slug` — Get a single person (frontmatter + full markdown body)
- `POST /api/peeps` — Create a new person (generate slug from name, write .md file)
- `PATCH /api/peeps/:slug` — Update a person (update frontmatter and/or body)
- `DELETE /api/peeps/:slug` — Delete a person (remove .md file)

**Requirements:**
- Use `gray-matter` npm package to parse/stringify markdown frontmatter
- Auto-create `/data/peeps/` directory if it doesn't exist
- Generate URL-safe slugs from names (lowercase, hyphenated)
- Return proper error codes (400 for missing required fields, 404 for not found)
- Add CORS middleware for local dev

**Test:** Create a person via POST, retrieve via GET, verify the .md file exists on disk with correct frontmatter.

### Task 2: Seed Data
Create 5 example people as markdown files in `/data/peeps/` so the UI has data to display immediately.

**People to create:**
1. A close friend with a birthday this month (to test upcoming birthday logic)
2. A family member with full contact info
3. A coworker with minimal info (just name and a note)
4. Someone with multiple tags
5. Someone with a birthday today (to test "today" highlight)

Each file should have realistic frontmatter and 2-3 lines of natural-sounding notes.

**Test:** GET /api/peeps returns 5 people with correct data.

### Task 3: People Grid UI
Build the main page that displays all people as cards in a responsive grid.

**Requirements:**
- Use shadcn/ui `Card` component for each person
- Show: name, birthday (formatted nicely), tags as `Badge` components, and a preview of their notes (first 100 chars)
- Responsive grid: 1 column on mobile, 2 on tablet, 3 on desktop
- Cards should be clickable — clicking opens a detail view (Task 5)
- If a person's birthday is today, show a visual indicator (a small cake icon or colored border)
- If a person's birthday is within the next 7 days, show "Birthday in X days" badge
- Sort: upcoming birthdays first by default
- Add Vite proxy config to forward `/api` requests to the Express server on port 3001

**Test:** App loads, displays 5 seed people as cards, responsive layout works, birthday indicators appear correctly.

### Task 4: Add & Edit Person
Build forms to add a new person and edit an existing person.

**Add Person:**
- Button at the top of the grid: "+ Add Person"
- Opens a shadcn/ui `Dialog` with a form
- Fields: Name (required), Birthday (date picker using shadcn Calendar), Phone, Email, Tags (comma-separated input), Notes (textarea)
- On submit: POST to /api/peeps, close dialog, refresh grid
- Show toast/alert on success

**Edit Person:**
- Edit button on each card (or in the detail view)
- Opens same dialog pre-filled with existing data
- On submit: PATCH to /api/peeps/:slug, close dialog, refresh grid

**Test:** Add a new person via the form, verify they appear in the grid and the .md file exists. Edit a person, verify changes persist.

### Task 5: Person Detail View & Delete
Build a detail view for a single person and the ability to delete.

**Detail View:**
- Clicking a card opens a detail panel (either a full-width dialog or a slide-over panel)
- Shows all frontmatter fields formatted nicely
- Shows full markdown notes rendered as HTML (use a simple markdown renderer)
- Edit button that opens the edit dialog (Task 4)
- Delete button with confirmation dialog

**Delete:**
- "Delete" button on detail view
- Shows shadcn/ui `AlertDialog`: "Are you sure you want to remove [Name]?"
- On confirm: DELETE /api/peeps/:slug, close detail view, refresh grid
- Show toast on success

**Test:** Open a person's detail view, verify all info displays. Delete a person, verify they're removed from grid and .md file is gone.

### Task 6: Search & Filter
Add the ability to search and filter people.

**Search:**
- Search input at the top of the page (shadcn/ui `Input`)
- Filters cards in real-time by name, email, notes content
- Debounced (300ms) for performance

**Filter by tag:**
- Show all unique tags as clickable filter chips below the search bar
- Clicking a tag filters to only people with that tag
- Can select multiple tags (AND logic)
- "Clear filters" button to reset

**Test:** Search for a name, verify correct filtering. Filter by tag, verify correct results. Clear filters, verify all people show.
