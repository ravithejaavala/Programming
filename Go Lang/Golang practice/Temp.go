package main

// "go mod init --file name--" to initalise 'go.mod' file, then only the go files are able to run
import (
	"fmt"
	"strings"
)

func main() {

	var remainTickets = 50
	userfname, userlname, userEmail, userTickets := userinputs()
	isValidname, isValidemail, isValidtickets := validateuser(userfname, userlname, userEmail, userTickets, remainTickets)

	fmt.Printf("name : %v\n", isValidname)
	fmt.Printf("email : %v\n", isValidemail)
	fmt.Printf("tickets : %v\n", isValidtickets)

	/*
		if isValidname {
			fmt.Printf("You entered First name or Last name is too short\n")
		}
		if isValidemail {
			fmt.Printf("You entered Email doesn't contain '@'\n")
		}
		if isValidtickets {
			fmt.Printf("You entered NO.of Tickets is invalid\n")
		}
	*/
}
func userinputs() (string, string, string, int) {
	var userfname string
	var userlname string
	var userEmail string
	var userTickets int

	fmt.Print("Enter your first name : ")
	fmt.Scan(&userfname)

	fmt.Print("Enter your last name : ")
	fmt.Scan(&userlname)

	fmt.Print("Enter your Email ID : ")
	fmt.Scan(&userEmail)

	fmt.Print("Enter the no.of Tickets you want : ")
	fmt.Scan(&userTickets)

	return userfname, userlname, userEmail, userTickets
}

func validateuser(userfname string, userlname string, userEmail string, userTickets int, remainTickets int) (bool, bool, bool) {
	isValidname := len(userfname) >= 2 && len(userlname) >= 2

	isValidemail := strings.Contains(userEmail, "@")

	isValidtickets := userTickets > 0 && userTickets <= remainTickets

	return isValidname, isValidemail, isValidtickets
}
