# Final Project Requirements

1. Build a web application using Django.
	- Create a dedicated project and at least one reusable app following Django conventions.
2. Define at least two related models that capture your core domain data and link them via a foreign key or many-to-many relationship.
	- Include helpful `__str__` representations and specify verbose names where useful.
3. Implement full CRUD functionality (create, read, update, delete) for the primary model through Django views.
	- Provide separate views (or combined class-based views) for listing, creating, updating, and deleting records.
4. Provide user-facing forms or interfaces for all CRUD operations.
	- Use `ModelForm` classes or form classes to handle validation and rendering.
5. Include basic validation and error handling for user input and database interactions.
	- Surface validation errors back to users and guard against invalid submissions in the views.
6. Demonstrate use of templates for rendering HTML responses.
	- Employ a base template with content blocks to avoid duplication and include navigation between CRUD pages.
7. Add minimal styling to ensure the UI is usable and coherent.
	- Bundle a simple CSS file (or utility framework) that keeps forms aligned and key actions visible.
8. Document setup, migration, and run instructions in the project README.
	- Cover dependencies, environment variables, migration commands, superuser creation, and how to launch the development server.
9. Document how the two models interact within your README to guide reviewers.
	- Outline the relationships using bullet points or a short diagram so reviewers understand the data flow.

## Optional Enhancements

- Include automated tests that cover the core CRUD workflows.
- Provide a Docker-based PostgreSQL setup for developers who prefer running against Postgres.

## Preset Project Ideas

1. **Online shop**
	 - Models
		 - Product for catalog items.
		 - Order as the customer transaction record.
		 - OrderItem with foreign keys to Product and Order to capture quantities and prices.
	 - Views
		 - Catalog list/detail pages for browsing products.
		 - Cart management for create/update/delete on OrderItems.
		 - Order summary page that finalizes the order.
	 - Optional tasks
		 - Add user authentication so shoppers can review order history.
		 - Build an inventory report view that highlights low-stock products.
2. **Weather dashboard**
	 - Models
		 - City representing locations being tracked.
		 - Observation with a foreign key to City storing timestamped temperature and conditions.
	 - Views
		 - City watchlist management.
		 - Observation entry form to log new data.
		 - City detail view charting historical readings.
	 - Optional tasks
		 - Integrate a third-party weather API for automatic observation imports.
		 - Schedule periodic summary emails highlighting notable weather changes.
3. **Event planner**
	 - Models
		 - Venue describing event locations.
		 - Event with a foreign key to Venue.
		 - RSVP linking Event to an Attendee model to track response status.
	 - Views
		 - Event create/edit forms.
		 - RSVP management screens.
		 - Venue calendar showing upcoming events.
	 - Optional tasks
		 - Provide ICS calendar export for events.
		 - Add waitlist support when an event reaches capacity.
