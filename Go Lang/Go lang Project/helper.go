package main

import (
	"fmt"
	"strings"
)

func greetusers() {
	fmt.Printf("Welcome to %v Booking Application\n", confName)
	fmt.Printf("We have total of %v tickets ,Now the available tickets are %v\n", confTickets, remainTickets)
	fmt.Printf("Buy your tickets to attend %v\n", confName)
}
func validateuser(userfname string, userlname string, userEmail string, userTickets int) (bool, bool, bool) {
	// in above line we defined the return data types "bool" multiple times, because this is compulsary for no.of values you are returning
	// And they are in other paranthasis , when they are multiple
	isValidname := len(userfname) >= 2 && len(userlname) >= 2
	// validating the useer input
	isValidemail := strings.Contains(userEmail, "@")
	// Validating the user email contains '@'
	isValidtickets := userTickets > 0 && userTickets <= remainTickets
	// using AND and OR operations in above and below respectively
	// isValidcity := userCity == "tirupati" || userCity == "chittoor"
	return isValidname, isValidemail, isValidtickets
	//***In Go we can return multiple values, other than any any other languages
}
