# ShelfMaster

This web application serves as a management system for a local library, aimed at simplifying the librarian's tasks. It allows the librarian to track books, their quantities, books issued to members, and book fees. For the sake of simplicity, it is assumed that the application will be used solely by the librarian, and therefore sessions and roles are not implemented.

## Functionality

### Base Library System

Librarians can maintain the following:

- **Books**: Manage books with maintained stock.
- **Members**: Maintain a list of library members.
- **Transactions**: Track transactions such as book issuances and returns.

### Use Cases

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on both Books and Members.
- **Book Issuance**: Issue a book to a library member.
- **Book Return**: Accept book returns from members and charge rental fees.
- **Search**: Search for a book by name and author.
- **Fee Management**: Ensure a member’s outstanding debt does not exceed KES. 500.