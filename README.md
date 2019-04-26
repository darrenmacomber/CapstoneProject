# MediaShelf (placeholder)

## Concept
An app designed to accommodate group reading and watching of media. Similar to GoodReads, basic functionality will allow for making a personalized profile that keeps track of what books you read, where you are in them, and how much you liked them. You can post blog entries about your experiences with the work and others can search and find them by keywords for your blog or the books you read. Other accounts can discuss with you by commenting on your posts. You will be able to filter out comments and profiles regarding works you're reading by accounts that are recorded as being further in the work than you are, avoiding spoilers.

## Functionality
(Start with just books then expand to other types of media)
* Media Blog
* Personalized profile pages
  - Bio
  - Blog and comment section
  - Works consumed
  - Ratings for books consumed
  - History and progress through books
* Customize who can access your profile and who can comment/ whose profiles you can see based on their history.
* Calendar, useful for keeping up with TV or chapters released on a schedule.
* Search function

## Libraries/Frameworks
Using an API that has publishing info to fill book data. (Author, publishing date, etc.)

## Apps
* LoginApp
  - Username
  - Password
  - Access Privileges
* ProfileApp
  - Associated User
  - Bio/personal info/book preferences (Can make specific fields searchable)
  - Schedule (Books you're interested in reading, schedule progress)
  - Blog
* BookApp
  - Associated API data
  - Brief description
  - Book data (Searchable tags, publish date, language, length)
  - Cover images
  - Activity history (Number of readers, how many/how much finished, links to public Profile Pages)
* SiteApp
  - Index Page and other templates
  - Main field (Recent additions to Books)
  - Chat field (Recent posts by public Profile Pages)
  - Search function (Books, public Profile Pages w/ tag)
* SearchApp
  - Main Field (List of results, type (Book/Profile))
  - Customize search to include any portion of or exact terms
  - Preset Searches (Most popular, most recently added, most completed)
  - Random book function

## Back-End/Data
* Profile database
  - Access permissions
  - Bio info/tags
* Book database
  - Book info sourced from API
  - Book activity history
  - User applied tags
* ProfileBook
  - Profile ID (ForeignKey)
  - Book ID (ForeignKey)
  - PercentCompleted (int)
  - Rating (int)
  - Date Started
  - Date Completed
* Tag
  - Text
  - Profile (ManyToMany)

## Schedule

### Milestone 1 Goals
  - [ ] User login
  - [ ] Set up Book model
  - [ ] Link in API to populate database for Book Model
  - [ ] Index for book
  - [ ] Model for Profile
  - [ ] Let user save Books to Profile and create ProfileBook Model
  - [ ] Templates
### Week 2 Goals
  - [ ] Blog function
  - [ ] Blog Post
  - [ ] Blog Comment
  - [ ] Tag and search function
  - [ ] Templates
### Week 3 Goals
  - [ ] Filtering tags and users
  - [ ] Following profiles
  - [ ] Schedule, Calender
