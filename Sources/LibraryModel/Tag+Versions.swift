//
// Tag+Versions.swift
// Created by Paul Schifferer on 6/16/21.
//

import Fluent


public extension Tag {
    enum v20210828 {
        // schema
        static let schemaName = "tags"

        // properties
        static let name = FieldKey(stringLiteral: "name")
        static let deletedAt = FieldKey(stringLiteral: "deletedAt")
        static let createdAt = FieldKey(stringLiteral: "createdAt")
        static let updatedAt = FieldKey(stringLiteral: "updatedAt")
    }
}